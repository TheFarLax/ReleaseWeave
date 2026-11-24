import json
import pytest


def test_window_all_acknowledgments_and_guide_lock(direct_deploy, direct_vm, direct_bob, direct_charlie, model, consensus):
    c = direct_deploy("deprecation_pact.py")
    item = c.open("v1", "v2", 10, 100, 90)
    with direct_vm.prank(direct_bob):
        c.enroll(item)
    with direct_vm.prank(direct_charlie):
        c.enroll(item)
    model("COMPLETE")
    c.lock_guide(item, "Full migration procedure.")
    consensus("GAP")
    with direct_vm.prank(direct_bob):
        c.acknowledge(item)
        with pytest.raises(Exception, match="already acknowledged"):
            c.acknowledge(item)
    with pytest.raises(Exception, match="has not acknowledged"):
        c.retire(item, 100)
    with direct_vm.prank(direct_charlie):
        c.acknowledge(item)
    with pytest.raises(Exception, match="cutoff"):
        c.retire(item, 99)
    c.retire(item, 100)
    assert json.loads(c.get(item))["state"] == "RETIRED"


def test_short_window_and_incomplete_guide(direct_deploy, direct_vm, direct_bob, model):
    c = direct_deploy("deprecation_pact.py")
    with pytest.raises(Exception, match="too short"):
        c.open("v1", "v2", 10, 20, 11)
    item = c.open("v1", "v2", 10, 20, 10)
    with direct_vm.prank(direct_bob):
        c.enroll(item)
    model("GAP")
    c.lock_guide(item, "Just upgrade.")
    with direct_vm.prank(direct_bob), pytest.raises(Exception, match="not ready"):
        c.acknowledge(item)

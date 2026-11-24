import json
import pytest


def test_confirmation_counts_distinct_reporter_wallets(direct_deploy, direct_vm, direct_bob, direct_charlie, model, consensus):
    c = direct_deploy("repro_quorum.py")
    item = c.open("abc", "Linux Python 3.12", "Run parse empty input. It crashes instead of returning empty.")
    with pytest.raises(Exception, match="own issue"):
        c.report(item, "abc", "Linux", "Crash")
    model("REPRODUCED")
    with direct_vm.prank(direct_bob):
        c.report(item, "abc", "Linux Python 3.12", "Same crash.")
        with pytest.raises(Exception, match="already participated"):
            c.report(item, "abc", "Linux", "Again.")
    consensus("NOT_REPRODUCED")
    with pytest.raises(Exception, match="two distinct"):
        c.confirm(item)
    with direct_vm.prank(direct_charlie):
        c.report(item, "abc", "Linux Python 3.12", "Same crash.")
    c.confirm(item)
    assert json.loads(c.get(item))["state"] == "CONFIRMED"


def test_different_version_cannot_count(direct_deploy, direct_vm, direct_bob):
    c = direct_deploy("repro_quorum.py")
    item = c.open("abc", "Linux", "Crash")
    with direct_vm.prank(direct_bob), pytest.raises(Exception, match="version differs"):
        c.report(item, "def", "Linux", "Crash")
    assert json.loads(c.get(item))["confirmations"] == 0

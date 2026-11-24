import json
import pytest


def test_adapter_review_must_pass_before_selection(direct_deploy, model, consensus):
    c = direct_deploy("dependency_exit.py")
    item = c.open("transport-v1", "Promise get returns bytes. Reject errors.")
    model("NEEDS_ADAPTER")
    candidate = c.review(item, "transport-v2", "Callback returns bytes and separate error.")
    consensus("DROP_IN")
    with pytest.raises(Exception, match="usable compatibility"):
        c.select(item, candidate)
    model("GAP")
    c.prove_adapter(item, candidate, "Just returns the body.")
    with pytest.raises(Exception, match="usable compatibility"):
        c.select(item, candidate)
    model("COMPLETE")
    c.prove_adapter(item, candidate, "Wrap callbacks in Promise and reject error callback.")
    consensus("GAP")
    c.select(item, candidate)
    assert json.loads(c.get(item))["selected"] == candidate
    with pytest.raises(Exception, match="already selected"):
        c.select(item, candidate)


def test_incompatible_candidate_cannot_get_adapter_shortcut(direct_deploy, model):
    c = direct_deploy("dependency_exit.py")
    item = c.open("cache", "Atomic compare-and-swap")
    model("INCOMPATIBLE")
    candidate = c.review(item, "file-cache", "Get and set only.")
    with pytest.raises(Exception, match="does not need"):
        c.prove_adapter(item, candidate, "Try a wrapper.")


def test_drop_in_can_be_selected_by_owner(direct_deploy, model, direct_vm, direct_bob):
    c = direct_deploy("dependency_exit.py")
    item = c.open("a", "returns bool")
    model("DROP_IN")
    candidate = c.review(item, "b", "returns bool")
    with direct_vm.prank(direct_bob), pytest.raises(Exception, match="maintainer"):
        c.select(item, candidate)
    c.select(item, candidate)

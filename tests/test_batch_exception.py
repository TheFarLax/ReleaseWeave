import json
import pytest


def test_only_declared_failed_rows_can_restore_the_batch(direct_deploy, direct_vm, direct_bob, model, consensus):
    c = direct_deploy("batch_exception.py")
    reviewer = "0x" + direct_bob.hex()
    item = c.open("batch", 10, "[4,8]", reviewer)
    with pytest.raises(Exception, match="not declared failed"):
        c.submit(item, 1, "Nonempty name.", "Name = Alex")
    c.submit(item, 4, "Nonempty name.", "Name = Alex")
    c.submit(item, 8, "Positive age.", "Age = 20")
    with pytest.raises(Exception, match="assigned reviewer"):
        c.adjudicate(item, 4)
    model("FIXED")
    with direct_vm.prank(direct_bob):
        c.adjudicate(item, 4)
        with pytest.raises(Exception, match="already adjudicated"):
            c.adjudicate(item, 4)
    consensus("STILL_FAILS")
    with pytest.raises(Exception, match="failed rows remain"):
        c.close(item)
    with direct_vm.prank(direct_bob):
        c.adjudicate(item, 8)
    c.close(item)
    state = json.loads(c.get(item))
    assert state["accepted"] + state["failed"] == state["total"] == 10
    assert state["state"] == "CLOSED"


def test_bad_row_list_is_rejected(direct_deploy, direct_bob):
    c = direct_deploy("batch_exception.py")
    for rows in ("[1,1]", "[0]", "[11]", "[true]"):
        with pytest.raises(Exception):
            c.open("batch", 10, rows, "0x" + direct_bob.hex())
    assert c.count() == 0


def test_retry_preserves_previous_rejection_and_count(direct_deploy, direct_vm, direct_bob, model):
    c = direct_deploy("batch_exception.py")
    item = c.open("batch", 5, "[2]", "0x" + direct_bob.hex())
    c.submit(item, 2, "Age > 0", "Age = -1")
    model("STILL_FAILS")
    with direct_vm.prank(direct_bob):
        c.adjudicate(item, 2)
    c.retry(item, 2, "Age = 10")
    model("FIXED")
    with direct_vm.prank(direct_bob):
        c.adjudicate(item, 2)
    state = json.loads(c.get(item))
    assert [x["review"] for x in state["exceptions"]["2"]["history"]] == ["STILL_FAILS", "FIXED"]
    assert state["accepted"] == 5 and state["failed"] == 0
    with pytest.raises(Exception, match="only rejected"):
        c.retry(item, 2, "Age = 10")

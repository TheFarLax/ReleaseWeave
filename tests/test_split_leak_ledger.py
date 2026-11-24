import json
import pytest


def test_freeze_requires_every_cross_partition_pair(direct_deploy, model, consensus):
    c = direct_deploy("split_leak_ledger.py")
    item = c.open("test")
    c.add(item, "TRAIN", "Add 2 and 3.")
    c.add(item, "TEST", "Name the largest ocean.")
    c.add(item, "TEST", "Translate cat to French.")
    model("DISTINCT")
    c.compare(item, 0, 1)
    consensus("SAME_ITEM")
    with pytest.raises(Exception, match="unresolved or leaked"):
        c.freeze(item)
    c.compare(item, 0, 2)
    c.freeze(item)
    assert json.loads(c.get(item))["state"] == "FROZEN"
    with pytest.raises(Exception, match="frozen"):
        c.add(item, "TRAIN", "Another task.")


def test_exact_duplicate_is_detected_without_model(direct_deploy):
    c = direct_deploy("split_leak_ledger.py")
    item = c.open("test")
    c.add(item, "TRAIN", "Same sample")
    c.add(item, "TEST", "Same sample")
    assert c.compare(item, 0, 1) == "SAME_ITEM"
    with pytest.raises(Exception, match="unresolved or leaked"):
        c.freeze(item)


def test_curator_and_partition_checks(direct_deploy, direct_vm, direct_bob):
    c = direct_deploy("split_leak_ledger.py")
    item = c.open("test")
    with direct_vm.prank(direct_bob), pytest.raises(Exception, match="curator"):
        c.add(item, "TRAIN", "task")
    with pytest.raises(Exception, match="unknown partition"):
        c.add(item, "VALIDATION", "task")

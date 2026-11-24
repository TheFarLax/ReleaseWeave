import json
import pytest


def test_committing_one_proposal_invalidates_the_other(direct_deploy, model, consensus):
    c = direct_deploy("migration_fence.py")
    item = c.open("customers", "id, name", "Preserve id and name.")
    model("LOSSLESS")
    one = c.propose(item, 1, "id, display_name", "Rename with backward backup.")
    two = c.propose(item, 1, "id, full_name", "Rename with reversible mapping.")
    consensus("LOSSY")
    assert c.commit(item, one, False) == 2
    with pytest.raises(Exception, match="stale schema"):
        c.commit(item, two, False)
    assert json.loads(c.get(item))["schema"] == "id, display_name"


@pytest.mark.parametrize("decision", ["BLOCKED", "UNCLEAR", "LOSSY"])
def test_unsafe_migration_is_gated(direct_deploy, model, direct_vm, direct_bob, decision):
    c = direct_deploy("migration_fence.py")
    item = c.open("dataset", "id, secret", "Preserve id.")
    model(decision)
    proposal = c.propose(item, 1, "id", "Drop secret.")
    with pytest.raises(Exception, match="acceptable review"):
        c.commit(item, proposal, False)
    with direct_vm.prank(direct_bob), pytest.raises(Exception, match="only dataset owner"):
        c.commit(item, proposal, True)
    if decision == "LOSSY":
        assert c.commit(item, proposal, True) == 2
    else:
        with pytest.raises(Exception, match="acceptable review"):
            c.commit(item, proposal, True)

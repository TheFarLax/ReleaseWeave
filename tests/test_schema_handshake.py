import json
import pytest


def test_provider_revision_expires_old_offers_and_current_agreements(direct_deploy, direct_vm, direct_bob, model, consensus):
    c = direct_deploy("schema_handshake.py")
    item = c.open("id int, name str")
    model("COMPATIBLE")
    with direct_vm.prank(direct_bob):
        first = c.propose(item, 1, "Requires id and name. Extra fields OK.")
        second = c.propose(item, 1, "Requires id. Extra fields OK.")
    consensus("INCOMPATIBLE")
    agreement = c.accept(item, first)
    assert c.agreement_current(item, agreement)
    c.revise(item, 1, "id string, name str")
    assert not c.agreement_current(item, agreement)
    with pytest.raises(Exception, match="stale consumer offer"):
        c.accept(item, second)
    assert json.loads(c.get(item))["agreements"][0]["schema"] == "id int, name str"


def test_incompatible_offer_cannot_be_accepted(direct_deploy, direct_vm, direct_bob, model):
    c = direct_deploy("schema_handshake.py")
    item = c.open("id string")
    with pytest.raises(Exception, match="cannot act as consumer"):
        c.propose(item, 1, "Requires id int")
    model("INCOMPATIBLE")
    with direct_vm.prank(direct_bob):
        offer = c.propose(item, 1, "Requires id int")
    with pytest.raises(Exception, match="compatible review"):
        c.accept(item, offer)

import json
import pytest


def test_full_regression_evidence_can_be_sealed(direct_deploy, model, consensus):
    c = direct_deploy("regression_witness.py")
    item = c.open("Empty parse crashes.", "abc", "def")
    model("WITNESS")
    test = c.evaluate(item, "assert parse('') == []", "abc: fails assertion", "def: passes assertion")
    consensus("BAD_TRANSITION")
    c.seal(item, test)
    assert json.loads(c.get(item))["selected"] == test
    with pytest.raises(Exception, match="already sealed"):
        c.evaluate(item, "test", "before", "after")


@pytest.mark.parametrize("decision", ["WEAK_ASSERTION", "BAD_TRANSITION", "UNCLEAR"])
def test_inadequate_test_cannot_become_the_witness(direct_deploy, model, decision):
    c = direct_deploy("regression_witness.py")
    item = c.open("Empty parse crashes.", "abc", "def")
    model(decision)
    test = c.evaluate(item, "assert True", "import failed", "import succeeded")
    with pytest.raises(Exception, match="lacks a regression"):
        c.seal(item, test)

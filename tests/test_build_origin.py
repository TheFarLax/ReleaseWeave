import json
import pytest


@pytest.mark.parametrize("different", [False, True])
def test_seal_requires_two_qualified_builders_and_checks_exact_hashes(direct_deploy, direct_vm, direct_bob, direct_charlie, model, consensus, different):
    c = direct_deploy("build_origin.py")
    item = c.open("abc", "Build wheel.", "Linux Python 3.12")
    model("QUALIFIED")
    with direct_vm.prank(direct_bob):
        c.attest(item, "a" * 64, "Run abc in environment.")
        with pytest.raises(Exception, match="already attested"):
            c.attest(item, "a" * 64, "Repeated.")
    consensus("MISMATCH")
    with pytest.raises(Exception, match="two qualified"):
        c.seal(item)
    with direct_vm.prank(direct_charlie):
        c.attest(item, ("b" if different else "a") * 64, "Run abc in environment.")
    assert c.seal(item) == ("CONTESTED" if different else "REPRODUCED")
    state = json.loads(c.get(item))
    assert state["artifact_sha256"] == ("" if different else "a" * 64)


def test_publisher_is_excluded_and_bad_hash_rejected(direct_deploy, direct_vm, direct_bob):
    c = direct_deploy("build_origin.py")
    item = c.open("abc", "Build.", "Linux")
    with pytest.raises(Exception, match="own build"):
        c.attest(item, "a"*64, "Evidence.")
    with direct_vm.prank(direct_bob), pytest.raises(Exception, match="invalid SHA"):
        c.attest(item, "short", "Evidence.")

import json
import pytest


def test_published_snapshot_survives_revision_and_old_reviews_expire(direct_deploy, model, consensus):
    c = direct_deploy("locale_parity.py")
    item = c.open("Use two batteries.")
    model("PARITY")
    c.review(item, 1, "fr", "Utilisez deux piles.")
    consensus("CONTRADICTED")
    c.publish(item, 1, '["fr"]')
    c.revise(item, 1, "Use three batteries.")
    with pytest.raises(Exception, match="stale source"):
        c.publish(item, 1, '["fr"]')
    with pytest.raises(Exception, match="parity review"):
        c.publish(item, 2, '["fr"]')
    state = json.loads(c.get(item))
    assert state["published"][0]["source"] == "Use two batteries."
    assert state["translations"] == {}


@pytest.mark.parametrize("decision", ["OMITTED", "CONTRADICTED", "UNCLEAR"])
def test_materially_changed_translation_cannot_publish(direct_deploy, model, decision):
    c = direct_deploy("locale_parity.py")
    item = c.open("Do not open before cooling for 10 minutes.")
    model(decision)
    c.review(item, 1, "fr", "Open immediately.")
    with pytest.raises(Exception, match="parity review"):
        c.publish(item, 1, '["fr"]')
    with pytest.raises(Exception, match="duplicate locale"):
        c.publish(item, 1, '["FR", "fr"]')

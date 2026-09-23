"""Empty set is a letter. Faustini is not the front. No live SPICE."""

from __future__ import annotations

from .frontier import gate

OFFER = "Unsigned. Not an invoice."
BAND = (-90.0, -80.0)


def empty_letter(ask: str, passers: list[str]) -> dict:
    empty = len(passers) == 0
    body = (
        "FEASFRONT. Polar lighting is a constraint inside the solver. It is not the app. "
        "Empty set is a letter. Faustini is off the front. No live SPICE. Not a globe."
        if empty
        else (
            "FEASFRONT. Named passers only. Pareto among sites that do not kill the mission. "
            "Hours declared, not SPICE. Faustini is not the front."
        )
    )
    return {
        "ask": ask,
        "empty": empty,
        "passers": passers,
        "body": body,
        "words": len(body.split()),
        "band": BAND,
        "spice": False,
        "offer": OFFER,
    }


def score_site(site_id: str, science: float, sun_ok: bool, slope_ok: bool) -> dict:
    s = gate(site_id, science, {"sun": sun_ok, "slope": slope_ok})
    return {"site_id": s.site_id, "ok": s.ok, "fails": s.fails, "science": s.science}

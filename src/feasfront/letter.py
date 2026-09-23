# Copyright 2026 Digital Currensy Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


def score_site(
    site_id: str,
    science: float,
    slope_deg: float | None,
    sun_hours: float | None,
    earth_hours: float | None,
    night_hours: float | None,
    *,
    max_slope_deg: float,
    min_sun_hours: float,
    min_earth_hours: float,
    max_night_hours: float,
) -> dict:
    scored = gate(
        site_id,
        science,
        slope_deg,
        sun_hours,
        earth_hours,
        night_hours,
        max_slope_deg=max_slope_deg,
        min_sun_hours=min_sun_hours,
        min_earth_hours=min_earth_hours,
        max_night_hours=max_night_hours,
    )
    return {
        "site_id": scored.site_id,
        "ok": scored.ok,
        "fails": scored.fails,
        "science": scored.science,
    }

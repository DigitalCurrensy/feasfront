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

"""Owned constraint gate. Tiny on purpose."""
from dataclasses import dataclass

@dataclass
class SiteScore:
    site_id: str
    ok: bool
    fails: list[str]
    science: float


def gate(
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
) -> SiteScore:
    if None in (slope_deg, sun_hours, earth_hours, night_hours):
        return SiteScore(site_id=site_id, ok=False, fails=["missing"], science=science)
    fails: list[str] = []
    if slope_deg > max_slope_deg:
        fails.append("slope")
    if sun_hours < min_sun_hours:
        fails.append("sun")
    if earth_hours < min_earth_hours:
        fails.append("earth")
    if night_hours > max_night_hours:
        fails.append("night")
    return SiteScore(site_id=site_id, ok=not fails, fails=fails, science=science)

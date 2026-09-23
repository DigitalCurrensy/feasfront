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

"""Flat-horizon hours. Spherical Moon. No terrain. No libration."""

from __future__ import annotations

import math

SYNODIC_HOURS = 29.530588853 * 24.0


def solar_elevation_deg(
    lat_deg: float,
    lon_deg: float,
    subsolar_lat_deg: float,
    subsolar_lon_deg: float,
) -> float:
    lat = math.radians(lat_deg)
    lon = math.radians(lon_deg)
    slat = math.radians(subsolar_lat_deg)
    slon = math.radians(subsolar_lon_deg)
    sine = (
        math.sin(lat) * math.sin(slat)
        + math.cos(lat) * math.cos(slat) * math.cos(lon - slon)
    )
    sine = max(-1.0, min(1.0, sine))
    return math.degrees(math.asin(sine))


def sun_hours(
    lat_deg: float,
    lon_deg: float,
    duration_hours: float,
    horizon_deg: float = 0.0,
    subsolar_lat_deg: float = 0.0,
    start_subsolar_lon_deg: float = 0.0,
    step_hours: float = 1.0,
) -> float:
    if duration_hours <= 0 or step_hours <= 0:
        raise ValueError("not enough")
    hours = 0.0
    t = 0.0
    while t < duration_hours - 1e-12:
        dt = min(step_hours, duration_hours - t)
        sub_lon = start_subsolar_lon_deg + 360.0 * (t / SYNODIC_HOURS)
        elevation = solar_elevation_deg(lat_deg, lon_deg, subsolar_lat_deg, sub_lon)
        if elevation > horizon_deg:
            hours += dt
        t += step_hours
    return hours


def _central_angle_deg(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return math.degrees(2 * math.asin(min(1.0, math.sqrt(h))))


def earth_hours(
    lat_deg: float,
    lon_deg: float,
    duration_hours: float,
    horizon_deg: float = 0.0,
    sub_earth_lat_deg: float = 0.0,
    sub_earth_lon_deg: float = 0.0,
) -> float:
    if duration_hours <= 0:
        raise ValueError("not enough")
    elevation = 90.0 - _central_angle_deg(lat_deg, lon_deg, sub_earth_lat_deg, sub_earth_lon_deg)
    if elevation > horizon_deg:
        return duration_hours
    return 0.0


def night_hours(sun: float, duration: float) -> float:
    if sun < 0 or sun > duration:
        raise ValueError("not enough")
    return duration - sun

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

"""Apply caller-supplied slope and hour limits to a site table."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from .frontier import gate
from .light import earth_hours, night_hours, sun_hours


def _optional_float(text: str | None) -> float | None:
    if text is None:
        return None
    stripped = text.strip()
    if stripped == "":
        return None
    return float(stripped)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="feasfront",
        description="Drop landing sites that miss slope, sun, Earth-view, or night limits.",
    )
    parser.add_argument("csv_path")
    parser.add_argument("--max-slope", type=float, required=True)
    parser.add_argument("--min-sun", type=float, required=True)
    parser.add_argument("--min-earth", type=float, required=True)
    parser.add_argument("--max-night", type=float, required=True)
    parser.add_argument("--duration", type=float, default=24.0)
    parser.add_argument("--horizon", type=float, default=0.0)
    args = parser.parse_args(argv)
    path = Path(args.csv_path)
    try:
        handle = path.open(newline="", encoding="utf-8")
    except OSError:
        print(f"unreadable: {path}", file=sys.stderr)
        return 2
    with handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        geometric = "lat" in fields
        for row in reader:
            slope = _optional_float(row.get("slope_deg"))
            if geometric:
                try:
                    lat = float(row["lat"])
                    lon = float(row["lon"])
                    sun = sun_hours(lat, lon, args.duration, horizon_deg=args.horizon)
                    earth = earth_hours(lat, lon, args.duration, horizon_deg=args.horizon)
                    night = night_hours(sun, args.duration)
                except (TypeError, ValueError):
                    sun = earth = night = None
            else:
                sun = _optional_float(row.get("sun_hours"))
                earth = _optional_float(row.get("earth_hours"))
                night = _optional_float(row.get("night_hours"))
            scored = gate(
                row["site_id"].strip(),
                float(row["science"]),
                slope,
                sun,
                earth,
                night,
                max_slope_deg=args.max_slope,
                min_sun_hours=args.min_sun,
                min_earth_hours=args.min_earth,
                max_night_hours=args.max_night,
            )
            word = "ok" if scored.ok else " ".join(scored.fails)
            if geometric:
                print(f"{scored.site_id} {word} sun={sun:.6g} earth={earth:.6g} night={night:.6g}")
            else:
                print(f"{scored.site_id} {word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from feasfront.frontier import gate  # noqa: E402
from feasfront.letter import empty_letter, score_site  # noqa: E402

LIMITS = dict(
    max_slope_deg=15.0,
    min_sun_hours=100.0,
    min_earth_hours=10.0,
    max_night_hours=100.0,
)


class FrontierTests(unittest.TestCase):
    def test_all_four_pass(self) -> None:
        scored = gate("ridge", 0.82, 15, 100, 10, 100, **LIMITS)
        self.assertTrue(scored.ok)
        self.assertEqual(scored.fails, [])
        via_letter = score_site("ridge", 0.82, 8, 180, 30, 40, **LIMITS)
        self.assertTrue(via_letter["ok"])
        self.assertEqual(via_letter["fails"], [])
        self.assertEqual(via_letter["science"], 0.82)

    def test_slope_only(self) -> None:
        scored = gate("wall", 0.55, 15.1, 100, 10, 100, **LIMITS)
        self.assertFalse(scored.ok)
        self.assertEqual(scored.fails, ["slope"])

    def test_missing_measurement(self) -> None:
        scored = gate("gap", 0.4, None, 0, 0, 999, **LIMITS)
        self.assertFalse(scored.ok)
        self.assertEqual(scored.fails, ["missing"])

    def test_night_over_the_max(self) -> None:
        scored = gate("dark", 0.5, 15, 100, 10, 100.1, **LIMITS)
        self.assertFalse(scored.ok)
        self.assertEqual(scored.fails, ["night"])

    def test_every_limit_that_applies(self) -> None:
        scored = gate("bad", 0.1, 16, 99, 9, 101, **LIMITS)
        self.assertFalse(scored.ok)
        self.assertEqual(scored.fails, ["slope", "sun", "earth", "night"])

    def test_empty_set_of_sites(self) -> None:
        letter = empty_letter("impossible envelope", [])
        self.assertEqual(letter["passers"], [])
        self.assertTrue(letter["empty"])
        self.assertFalse(letter["spice"])
        self.assertLessEqual(letter["words"], 80)
        self.assertNotIn("recommend", letter["body"].lower())
        named = empty_letter("named passers", ["site-a"])
        self.assertFalse(named["empty"])
        self.assertEqual(named["passers"], ["site-a"])


if __name__ == "__main__":
    unittest.main()

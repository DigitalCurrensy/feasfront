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

from feasfront.letter import empty_letter, score_site  # noqa: E402


class FrontierTests(unittest.TestCase):
    def test_gate_and_empty_letter(self) -> None:
        ok = score_site("faustini", 0.9, sun_ok=True, slope_ok=True)
        self.assertTrue(ok["ok"])
        dead = score_site("faustini", 0.9, sun_ok=False, slope_ok=True)
        self.assertFalse(dead["ok"])
        self.assertEqual(dead["fails"], ["sun"])
        letter = empty_letter("impossible envelope", [])
        self.assertTrue(letter["empty"])
        self.assertFalse(letter["spice"])
        self.assertLessEqual(letter["words"], 80)
        named = empty_letter("named passers", ["site-a"])
        self.assertFalse(named["empty"])


if __name__ == "__main__":
    unittest.main()

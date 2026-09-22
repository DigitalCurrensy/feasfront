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

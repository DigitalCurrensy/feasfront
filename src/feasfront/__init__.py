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

"""FEASFRONT — polar lighting is a constraint inside the solver. It is not the app."""

from .frontier import SiteScore, gate
from .light import SYNODIC_HOURS, earth_hours, night_hours, solar_elevation_deg, sun_hours
from .letter import empty_letter, score_site

__all__ = ["SYNODIC_HOURS", "SiteScore", "earth_hours", "empty_letter", "gate", "night_hours", "score_site", "solar_elevation_deg", "sun_hours"]

# FEASFRONT

For a lander team that has to throw sites out before anyone calls a site selected.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited. The copyright notice is in NOTICE and at the top of each source file.

## What it decides

Pass, or out. If nothing survives, the empty set is a result. An empty passer list is a letter, not a recommendation.

## The rule

The caller can supply the hours. The desk can also compute them. Solar elevation uses sin(el) = sin(lat)sin(subsolar lat) + cos(lat)cos(subsolar lat)cos(lon difference). The subsolar longitude walks 360 degrees in 29.530588853 days. A step counts as sun when elevation is above the horizon. Earth hours are the whole duration when Earth elevation, 90 degrees minus the angle to the sub-Earth point, is above that horizon, and zero otherwise. Earth does not move. Night hours are the duration minus the sun hours. There is no terrain and no libration. The desk then applies the limits the caller names: maximum slope, minimum sun, minimum Earth view, and maximum night.

A missing measurement, a non-finite hour, or a non-finite latitude or longitude fails the site as `missing` and does not add the other gates. Otherwise every limit the numbers miss is reported, in order: `slope`, `sun`, `earth`, `night`. The site is ok only when that list is empty.

## Worked rows

`examples/sites.csv` has one passer, one slope failure, and one missing measurement. Those rows are not a NASA site selection.

## What it will not do

- Add terrain or libration.
- Fill a missing slope with a guess.
- Turn an empty list into a recommendation.

## Run

```
git clone <this repo>
cd feasfront
PYTHONPATH=src python -m unittest tests.test_kernel
PYTHONPATH=src python -m feasfront examples/sites.csv --max-slope 15 --min-sun 100 --min-earth 10 --max-night 100
PYTHONPATH=src python -m feasfront examples/geometry.csv --max-slope 15 --min-sun 1 --min-earth 1 --max-night 24 --duration 24
```

Python 3.11 or newer. No third-party packages. A site that fails still exits 0. An unreadable file exits 2.

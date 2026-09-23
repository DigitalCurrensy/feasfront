# FEASFRONT

For a lander team that has to throw sites out before anyone calls a site selected.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited. The copyright notice is in NOTICE and at the top of each source file. Cited data and papers stay with their authors.
## What it decides

Pass, or out. If nothing survives, the empty set is the result.

## The rule

Slope, sun, time in Earth view, and night. Each limit is a gate. The first miss removes the site. An impossible envelope is allowed to return nothing.

## Worked cases

Three envelopes against named polar sites stored here: a first operating envelope, a tight vehicle, and an ask that cannot be met. These are not a NASA site selection.

## What it will not do

- Paint a lighting map and call it a landing site.
- Fill a missing limit with a guess.
- Turn an empty list into a recommendation.

## Run

```
git clone <this repo>
cd feasfront
PYTHONPATH=src python -m unittest tests.test_kernel
```

Python 3.12. No third-party packages. The test is the demo.

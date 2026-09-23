# FEASFRONT

FEASFRONT takes a lander envelope and a list of sites and prints the sites that survive. If none survive, the empty set is the result.

**Owner:** Digital Currensy Inc.
**License:** Apache-2.0. Our code only. Cited maps and papers stay with their authors.

## What it decides

Pass, or out. A site must clear slope, illumination, time in Earth view, and night. Missing a limit is not a pass.

## The rule

Slope, sun, Earth hours, night. Each limit is a gate. The first failure removes the site. An impossible envelope is allowed to return nothing.

## Worked cases

Three envelopes against a named set of polar sites that live in this repository: a first operating envelope, a tight vehicle, and an ask that cannot be met. The names are the desk’s cases. They are not a NASA site selection.

## What it will not do

- Paint a lighting globe and call it a landing site.
- Fill a missing limit with a guess.
- Turn an empty list into a recommendation.

## Run

```
PYTHONPATH=src python -m unittest tests.test_kernel
```

Notes under `docs/` are the build record. This page is the description.

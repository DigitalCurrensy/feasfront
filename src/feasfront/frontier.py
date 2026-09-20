"""Owned constraint gate. Tiny on purpose."""
from dataclasses import dataclass

@dataclass
class SiteScore:
    site_id: str
    ok: bool
    fails: list[str]
    science: float


def gate(site_id: str, science: float, constraints: dict[str, bool]) -> SiteScore:
    fails = [name for name, passed in constraints.items() if not passed]
    return SiteScore(site_id=site_id, ok=not fails, fails=fails, science=science)

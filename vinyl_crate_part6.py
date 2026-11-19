# === Stage 6: Связи между сущностями ===
# Project: VinylCrate
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Vinyl:
    title: str
    artist: str
    year: Optional[int] = None
    condition: str = "new"


@dataclass
class Listening:
    vinyl: Vinyl
    heard_at: Optional[str] = None


class VinylStore:
    def __init__(self) -> None:
        self._listings: Dict[object, List[Listening]] = {}

    def add_vinyl(self, vinyl: Vinyl) -> Vinyl:
        self._listings.setdefault(vinyl, [])
        return vinyl

    def add_listening(self, vinyl: Vinyl, heard_at: Optional[str] = None) -> Listening:
        vinyls = self._listings.setdefault(vinyl, [])
        listening = Listening(vinyl=vinyl, heard_at=heard_at)
        vinyls.append(listening)
        return listening

    def get_listings_for(self, vinyl: Vinyl) -> List[Listening]:
        return list(self._listings.get(vinyl, []))

    def check_integrity(self, vinyl: Vinyl) -> bool:
        for listening in self.get_listings_for(vinyl):
            if listening.vinyl is not vinyl:
                return False
        return True

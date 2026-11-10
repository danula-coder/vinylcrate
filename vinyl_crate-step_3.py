# === Stage 3: Хранилище в памяти ===
# Project: VinylCrate
memory_store.py

from typing import Dict, List, Any, Optional


class Vinyl:
    def __init__(self, title: str, artist: str, year: int, condition: str):
        self.id = None
        self.title = title
        self.artist = artist
        self.year = year
        self.condition = condition

    def __repr__(self):
        return f"Vinyl(id={self.id!r}, title={self.title!r})"


class VinylMemoryStore:
    def __init__(self):
        self._index: Dict[int, Vinyl] = {}
        self._counter = 1

    def add(self, vinyl: Vinyl) -> Vinyl:
        vinyl.id = self._counter
        self._counter += 1
        self._index[vinyl.id] = vinyl
        return vinyl

    def get(self, vinyl_id: int) -> Optional[Vinyl]:
        return self._index.get(vinyl_id)

    def list(self) -> List[Vinyl]:
        return list(self._index.values())

    def __len__(self):
        return len(self._index)


if __name__ == "__main__":
    store = VinylMemoryStore()

    a = Vinyl("Abbey Road", "The Beatles", 1969, "mint")
    b = Vinyl("Kind of Blue", "Miles Davis", 1959, "played")

    store.add(a)
    store.add(b)

    print(f"Добавлено пластинок: {len(store)}")

    print(f"Получили по id=1: {store.get(1)}")
    print(f"Получили по id=999: {store.get(999)}")

    print("Список:")
    for vinyl in store.list():
        print(f"  id={vinyl.id} {vinyl.title} — {vinyl.artist} ({vinyl.year}, {vinyl.condition})")

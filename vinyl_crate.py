# === Stage 1: Каркас модуля ===
# Project: VinylCrate
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

SHELL_CONDITIONS = ("mint", "near_mint", "very_good", "good", "fair", "poor")

@dataclass(frozen=True)
class VinylRecord:
    title: str
    artist: str
    year: int
    condition: str

    def __post_init__(self) -> None:
        if self.condition not in SHELL_CONDITIONS:
            raise ValueError(
                f"Неизвестное состояние '{self.condition}'. "
                f"Допустимые: {', '.join(SHELL_CONDITIONS)}"
            )

def make_demo_records() -> List[VinylRecord]:
    return [
        VinylRecord("The Dark Side of the Moon", "Pink Floyd", 1973, "very_good"),
        VinylRecord("Kind of Blue", "Miles Davis", 1959, "near_mint"),
        VinylRecord("Random Access Memories", "Daft Punk", 2013, "good"),
        VinylRecord("Blonde", "Frank Ocean", 2016, "mint"),
        VinylRecord("Nevermind", "Nirvana", 1991, "fair"),
    ]

def main() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("VinylCrate — коллекция пластинок")
    print(f"Каркас модуля запущен в {now}")
    print("-" * 40)
    for record in make_demo_records():
        print(f"{record.title}")
        print(f"  исполнитель: {record.artist}")
        print(f"  год: {record.year}")
        print(f"  состояние: {record.condition}")
        print("-" * 40)

if __name__ == "__main__":
    main()

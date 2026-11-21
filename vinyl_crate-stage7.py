# === Stage 7: Сортировка записей ===
# Project: VinylCrate
from datetime import datetime


def sort_by_title(records, reverse=False):
    return sorted(
        records,
        key=lambda record: record["name"].lower(),
        reverse=reverse,
    )


def sort_by_created_at(records, reverse=False):
    return sorted(
        records,
        key=lambda record: record["created_at"],
        reverse=reverse,
    )


def sort_records(records, field="name", reverse=False):
    if field == "created_at":
        return sort_by_created_at(records, reverse=reverse)
    return sort_by_title(records, reverse=reverse)


def build_records(names, created_at=None):
    created_at = created_at or datetime.now()
    return [
        {
            "name": name,
            "created_at": created_at,
        }
        for name in names
    ]


def demo():
    records = build_records(
        ["Pink Floyd", "Led Zeppelin", "The Beatles", "Nirvana"]
    )

    print("Исходный порядок:")
    for record in records:
        print(f"  {record['name']}")

    print("\nПо названию (возрастание):")
    for record in sort_records(records, reverse=False):
        print(f"  {record['name']}")

    print("\nПо названию (убывание):")
    for record in sort_records(records, reverse=True):
        print(f"  {record['name']}")

    print("\nПо дате создания (возрастание):")
    for record in sort_records(records, field="created_at", reverse=False):
        print(f"  {record['name']} ({record['created_at']})")

    print("\nПо дате создания (убывание):")
    for record in sort_records(records, field="created_at", reverse=True):
        print(f"  {record['name']} ({record['created_at']})")


if __name__ == "__main__":
    demo()

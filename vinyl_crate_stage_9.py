# === Stage 9: Постраничный вывод ===
# Project: VinylCrate
from typing import List, Dict, Any, Iterable


class Page:
    def __init__(self, page: int, items: List[Any]):
        self.page = page
        self.items = items

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


class Paginator:
    def __init__(self, page_size: int):
        if page_size <= 0:
            raise ValueError("Размер страницы должен быть положительным")
        self.page_size = page_size

    def paginate(self, records: Iterable[Any], page: int = 1) -> Page:
        page = max(page, 1)
        items = list(records)
        start = (page - 1) * self.page_size
        end = start + self.page_size
        return Page(page, items[start:end])

    def total_pages(self, count: int) -> int:
        return (count + self.page_size - 1) // self.page_size


def paginate_records(
    records: Iterable[Any], page_size: int, page: int = 1
) -> Page:
    paginator = Paginator(page_size)
    return paginator.paginate(records, page)


def parse_page_params(raw: Dict[str, Any]) -> Dict[str, Any]:
    page = int(raw.get("page", 1))
    page_size = int(raw.get("page_size", 10))
    return {"page": page, "page_size": page_size}


def collect_vinyls(vinyls: Iterable[Dict[str, Any]], page_size: int, page: int = 1) -> Page:
    def generator() -> Iterable[Dict[str, Any]]:
        for vinyl in vinyls:
            yield vinyl

    return paginate_records(generator(), page_size, page)


def page_info(page: Page) -> Dict[str, int]:
    return {
        "page": page.page,
        "size": len(page),
        "total_pages": page.total_pages,
    }

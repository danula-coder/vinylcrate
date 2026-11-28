# === Stage 10: Быстрые фильтры ===
# Project: VinylCrate
import datetime

TODAY = datetime.date.today()


def parse_date(value):
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    return datetime.date.fromisoformat(str(value)[:10])


def days_until_due(record):
    release = parse_date(getattr(record, "date_released", None)
                        or getattr(record, "year", None))
    if release is None:
        return None
    return (release - TODAY).days


def is_due_today(record):
    delta = days_until_due(record)
    return delta is not None and delta <= 7


def is_due_this_week(record):
    delta = days_until_due(record)
    return delta is not None and delta <= 14


def is_overdue(record):
    delta = days_until_due(record)
    return delta is not None and delta < 0


def filter_records(records, kind):
    if kind == "today":
        return [r for r in records if is_due_today(r)]
    if kind == "this_week":
        return [r for r in records if is_due_this_week(r)]
    if kind == "overdue":
        return [r for r in records if is_overdue(r)]
    raise ValueError("Неизвестный фильтр: %s" % kind)

# === Stage 4: Редактирование записей ===
# Project: VinylCrate
from typing import Optional


VALID_CONDITIONS = ("новый", "отличное", "хорошее", "удовлетворительное", "плохое")

EDITABLE_FIELDS = ("название", "исполнитель", "год", "состояние")


def validate_record_update(record: dict, updates: dict) -> Optional[str]:
    """Проверяет, что изменения допустимы; возвращает сообщение об ошибке или None."""
    unknown_fields = set(updates.keys()) - set(EDITABLE_FIELDS)
    if unknown_fields:
        return f"Недопустимые поля для редактирования: {', '.join(sorted(unknown_fields))}"

    invalid_year = updates.get("год")
    if invalid_year is not None:
        if not isinstance(invalid_year, int) or invalid_year < 1900 or invalid_year > 2100:
            return "Поле 'год' должно быть целым числом от 1900 до 2100"

    invalid_condition = updates.get("состояние")
    if invalid_condition is not None:
        if invalid_condition not in VALID_CONDITIONS:
            return f"Недопустимое состояние: '{invalid_condition}'. Допустимые: {', '.join(VALID_CONDITIONS)}"

    if not updates:
        return "Не указано ни одного поля для изменения"

    return None


def apply_record_update(record: dict, updates: dict) -> dict:
    """Применяет допустимые изменения к пластинке и возвращает обновлённую копию."""
    result = dict(record)
    result.update(updates)
    return result


def edit_record_by_id(records: dict, record_id: str, updates: dict) -> Optional[dict]:
    """Редактирует пластинку по идентификатору; возвращает обновлённую пластинку или None."""
    if record_id not in records:
        return None

    error = validate_record_update(records[record_id], updates)
    if error is not None:
        return error

    return apply_record_update(records[record_id], updates)

# === Stage 2: Проверка полей ===
# Project: VinylCrate
import re


VALID_STATES = ("новая", "очень хорошая", "хорошая", "удовлетворительная", "плохая")
VALID_YEAR_RE = re.compile(r"^\d{1,4}$")
NAME_MAX_LEN = 100
ARTIST_MAX_LEN = 100
TITLE_MAX_LEN = 200


def normalize_text(value):
    if value is None:
        return ""
    text = str(value).strip()
    return re.sub(r"\s+", " ", text)


def normalize_year(value):
    if value is None:
        return ""
    text = str(value).strip()
    if not VALID_YEAR_RE.match(text):
        return ""
    return text


def normalize_state(value):
    if value is None:
        return ""
    text = str(value).strip().lower()
    if text in VALID_STATES:
        return text
    return ""


def validate_name(value):
    name = normalize_text(value)
    if not name:
        return "", "Название пластинки не может быть пустым"
    if len(name) > NAME_MAX_LEN:
        return "", f"Название слишком длинное (максимум {NAME_MAX_LEN} символов)"
    return name, None


def validate_artist(value):
    artist = normalize_text(value)
    if not artist:
        return "", "Исполнитель не может быть пустым"
    if len(artist) > ARTIST_MAX_LEN:
        return "", f"Исполнитель слишком длинный (максимум {ARTIST_MAX_LEN} символов)"
    return artist, None


def validate_year(value):
    year = normalize_year(value)
    if not year:
        return "", "Укажите корректный год (число от 1 до 9999)"
    if int(year) > 9999:
        return "", "Год слишком большой (максимум 9999)"
    return year, None


def validate_state(value):
    state = normalize_state(value)
    if not state:
        return "", f"Неверное состояние пластинки. Доступные варианты: {', '.join(VALID_STATES)}"
    return state, None

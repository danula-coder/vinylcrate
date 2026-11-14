# === Stage 5: Удаление и восстановление ===
# Project: VinylCrate
def soft_delete_record(record, deleted_stores):
    record.deleted = True
    record.deleted_at = _utcnow()
    record.deleted_by = deleted_stores.get("user_id")
    record.deleted_at_all_records.append(_utcnow())
    return record

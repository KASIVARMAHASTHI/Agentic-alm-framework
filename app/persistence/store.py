from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class FileStore:
    def __init__(self, file_path: str = "data/workflow_state.json") -> None:
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def _read_all(self) -> List[Dict[str, Any]]:
        content = self.file_path.read_text(encoding="utf-8").strip()
        if not content:
            return []
        return json.loads(content)

    def _write_all(self, records: List[Dict[str, Any]]) -> None:
        self.file_path.write_text(json.dumps(records, indent=2), encoding="utf-8")

    def insert(self, record: Dict[str, Any]) -> Dict[str, Any]:
        records = self._read_all()
        records.append(record)
        self._write_all(records)
        return record

    def update_status(self, correlation_id: str, status: str) -> Dict[str, Any]:
        records = self._read_all()
        updated: Dict[str, Any] | None = None
        for record in records:
            if record.get("correlation_id") == correlation_id:
                record["workflow_status"] = status
                updated = record
        self._write_all(records)
        return updated or {"correlation_id": correlation_id, "workflow_status": "not_found"}

    def get_by_correlation_id(self, correlation_id: str) -> Dict[str, Any]:
        records = self._read_all()
        for record in records:
            if record.get("correlation_id") == correlation_id:
                return record
        return {"correlation_id": correlation_id, "workflow_status": "not_found"}

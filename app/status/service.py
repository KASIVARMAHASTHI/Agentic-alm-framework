from typing import Any, Dict

from app.persistence.store import FileStore


class StatusService:
    def __init__(self) -> None:
        self.store = FileStore()

    def create_workflow(self, record: Dict[str, Any]) -> Dict[str, Any]:
        record.setdefault("workflow_status", "received")
        return self.store.insert(record)

    def update_status(self, correlation_id: str, status: str) -> Dict[str, Any]:
        return self.store.update_status(correlation_id, status)

    def get_status(self, correlation_id: str) -> Dict[str, Any]:
        return self.store.get_by_correlation_id(correlation_id)

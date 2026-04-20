from collections import deque
from typing import Any, Deque, Dict, Optional


class ExecutionQueue:
    def __init__(self) -> None:
        self._queue: Deque[Dict[str, Any]] = deque()

    def enqueue(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self._queue.append(task)
        return {"queue_status": "enqueued", "queue_size": len(self._queue)}

    def dequeue(self) -> Optional[Dict[str, Any]]:
        if not self._queue:
            return None
        return self._queue.popleft()

    def size(self) -> int:
        return len(self._queue)

from typing import Any, Dict

from app.executor.queue import ExecutionQueue
from app.executor.retry import RetryPolicy
from app.executor.service import ExecutionService


class Worker:
    def __init__(self, queue: ExecutionQueue):
        self.queue = queue
        self.executor = ExecutionService()
        self.retry_policy = RetryPolicy()

    def process_next(self) -> Dict[str, Any]:
        task = self.queue.dequeue()
        if not task:
            return {"status": "no_tasks"}

        try:
            result = self.retry_policy.execute_with_retry(self.executor.execute, task)
            return {"status": "processed", "result": result}
        except Exception as e:
            return {"status": "failed", "error": str(e)}

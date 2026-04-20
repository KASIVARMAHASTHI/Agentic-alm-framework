from app.executor.queue import ExecutionQueue


class ExecutionService:
    def __init__(self):
        self.queue = ExecutionQueue()

    def execute(self, plan: dict) -> dict:
        # enqueue instead of direct execution
        enqueue_result = self.queue.enqueue(plan)
        return {
            "execution_status": "queued",
            "queue": enqueue_result
        }

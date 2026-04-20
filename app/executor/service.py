class ExecutionService:
    def execute(self, plan: dict) -> dict:
        return {
            "execution_status": "success",
            "steps_executed": plan.get("plan", [])
        }

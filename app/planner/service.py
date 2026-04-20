class PlannerService:
    def create_plan(self, normalized_payload: dict) -> dict:
        return {
            "plan": [
                "validate",
                "check_risk",
                "execute_action"
            ],
            "status": "planned"
        }

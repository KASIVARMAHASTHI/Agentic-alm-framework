class ApprovalService:
    def requires_approval(self, plan: dict) -> bool:
        return "check_risk" in plan.get("plan", [])

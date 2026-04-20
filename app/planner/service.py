from app.planner.catalog import get_actions


class PlannerService:
    def create_plan(self, normalized_payload: dict) -> dict:
        insight = normalized_payload.get("normalized_payload", {}).get("insight", {})

        insight_type = insight.get("type", "default")
        severity = insight.get("severity", "medium")

        actions = get_actions(insight_type, severity)

        return {
            "plan": actions,
            "metadata": {
                "insight_type": insight_type,
                "severity": severity
            },
            "status": "planned"
        }

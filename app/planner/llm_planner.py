from typing import Any, Dict

from app.planner.catalog import get_actions


class LLMPlannerService:
    """A lightweight planner interface that simulates an LLM-assisted planning step.

    In a production setup, this module can be connected to an external model provider.
    For now, it preserves a safe fallback to the catalog-driven planner.
    """

    def create_plan(self, normalized_payload: Dict[str, Any]) -> Dict[str, Any]:
        insight = normalized_payload.get("normalized_payload", {}).get("insight", {})
        insight_type = insight.get("type", "default")
        severity = insight.get("severity", "medium")
        confidence_score = insight.get("confidence_score", 0.0)

        # Production-safe fallback rule:
        # if confidence is low or unsupported type is received, rely on catalog planning.
        if confidence_score < 0.75:
            return {
                "plan": get_actions(insight_type, severity),
                "metadata": {
                    "planner": "catalog_fallback",
                    "reason": "low_confidence",
                    "insight_type": insight_type,
                    "severity": severity,
                },
                "status": "planned",
            }

        # Simulated LLM-style planning logic.
        suggested_actions = ["validate", f"analyze_{insight_type}"]
        if severity == "high":
            suggested_actions.append("check_risk")
        suggested_actions.append("execute_action")

        return {
            "plan": suggested_actions,
            "metadata": {
                "planner": "llm_simulated",
                "reason": "sufficient_confidence",
                "insight_type": insight_type,
                "severity": severity,
            },
            "status": "planned",
        }

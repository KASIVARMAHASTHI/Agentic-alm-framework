ACTION_CATALOG = {
    "threshold_breach": {
        "default": ["validate", "assess_threshold", "execute_action"],
        "high": ["validate", "assess_threshold", "check_risk", "execute_action"],
    },
    "anomaly": {
        "default": ["validate", "investigate_anomaly", "execute_action"],
        "high": ["validate", "investigate_anomaly", "check_risk", "execute_action"],
    },
    "recommendation": {
        "default": ["validate", "review_recommendation", "execute_action"],
        "high": ["validate", "review_recommendation", "check_risk", "execute_action"],
    },
}


def get_actions(insight_type: str, severity: str) -> list[str]:
    config = ACTION_CATALOG.get(insight_type, {})
    if severity == "high":
        return config.get("high", ["validate", "check_risk", "execute_action"])
    return config.get("default", ["validate", "execute_action"])

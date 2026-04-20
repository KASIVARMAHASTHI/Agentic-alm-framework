from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class Insight(BaseModel):
    insight_id: str = Field(..., description="Unique identifier for the insight")
    type: str = Field(..., description="Insight type such as threshold_breach or anomaly")
    description: str = Field(..., description="Human-readable description of the insight")
    metrics: Dict[str, Any] = Field(default_factory=dict, description="Associated metrics and values")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Confidence score from 0 to 1")
    severity: Optional[str] = Field(default="medium", description="Severity level such as low, medium, or high")


class InsightRequest(BaseModel):
    source_system: str = Field(..., description="System that generated the insight")
    source_agent: str = Field(..., description="Agent or module that emitted the insight")
    tenant_id: Optional[str] = Field(default=None, description="Optional tenant identifier")
    correlation_id: Optional[str] = Field(default=None, description="Optional correlation identifier")
    insight: Insight

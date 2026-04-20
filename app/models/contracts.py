from pydantic import BaseModel
from typing import Dict, Any


class Insight(BaseModel):
    insight_id: str
    type: str
    description: str
    metrics: Dict[str, Any]
    confidence_score: float

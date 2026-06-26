from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted insurance premium category",
        example="High"
    )
    confidence_scores: Dict[str, float] = Field(
        ...,
        description="Confidence scores for each predicted class",
        example={"Low": 0.01, "Medium": 0.15, "High": 0.84}
    )
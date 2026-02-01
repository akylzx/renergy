from pydantic import BaseModel
from typing import Dict, Any, List, Literal

class Requirement(BaseModel):
    energy_type: Literal["solar", "wind"]
    region: str
    min_area_acres: float
    criteria: Dict[str, float]
    constraints: Dict[str, Any]

class Site(BaseModel):
    lat: float
    lon: float
    score: float
    features: Dict[str, float]

class AnalysisResult(BaseModel):
    sites: List[Site]

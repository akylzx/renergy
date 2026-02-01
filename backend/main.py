from fastapi import FastAPI
from backend.schemas import Requirement, AnalysisResult
from backend.gemini import parse_requirements
from backend.gee import analyze, init_gee
from pydantic import BaseModel
import json

app = FastAPI(title="Renewable Site Finder")
init_gee()

@app.post("/parse", response_model=Requirement)
def parse(query: str):
    raw = parse_requirements(query)
    return Requirement.model_validate_json(raw)

@app.post("/analyze", response_model=AnalysisResult)
def analyze_sites(req: Requirement):
    sites = analyze(req)
    return {"sites": sites[:10]}


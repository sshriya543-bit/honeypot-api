from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List
import re


app = FastAPI(
    title="Agentic Honey-Fix API",
    description="Honeypot API to analyze scam messages and extract intelligence",
    version="1.0"
)


API_KEY = "HONEYFIX-1234"  


class ScamRequest(BaseModel):
    message: str

class ScamResponse(BaseModel):
    scam: bool
    phones: List[str]
    emails: List[str]
    urls: List[str]
    risk_level: str


@app.get("/")
def root():
    return {"status": "running", "message": "Honey-Fix API Live"}

@app.post("/analyze", response_model=ScamResponse)
def analyze_scam(
    data: ScamRequest,
    x_api_key: str = Header(...)   # <-- header required now
):
    try:

        if x_api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid or missing API key")

        text = data.message

       
        phones = re.findall(r"\b\d{10}\b", text)
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        urls = re.findall(r"https?://[^\s]+", text)

        scam_detected = bool(phones or emails or urls)
        risk = "HIGH" if scam_detected else "LOW"

        return {
            "scam": scam_detected,
            "phones": phones,
            "emails": emails,
            "urls": urls,
            "risk_level": risk
        }

    except Exception as e:
        
        raise HTTPException(status_code=500, detail=str(e))

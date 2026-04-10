from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.spidermail.ml.predict import SpiderMailPredictor


app = FastAPI(title="SpiderMail API")


class EmailRequest(BaseModel):
    text: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict")
def predict_email(payload: EmailRequest) -> dict:
    try:
        predictor = SpiderMailPredictor()
        result = predictor.predict(payload.text)
        return result
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

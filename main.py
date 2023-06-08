from fastapi import FastAPI
from pydantic import BaseModel

from utils.text_processing import normalize

class TextRequest(BaseModel):
    text: str

app = FastAPI()

@app.post("/normalize")
def normalize_text(request: TextRequest):
    normalized_text = normalize(request.text)
    return {"normalized_text": normalized_text}

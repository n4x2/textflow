from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.text_processing import normalize

class TextRequest(BaseModel):
    text: str

class StandardResponse(BaseModel):
    success: bool
    message: str
    data: dict = {}
    error_code: int = None

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.post("/normalize", response_model=StandardResponse)
def normalize_text(request: Request, payload: TextRequest):
    try:
        content_type = request.headers.get("Content-Type", "")
        if content_type.lower() != "application/json":
            raise HTTPException(status_code=415, detail="Unsupported Media Type. Only JSON is supported.")

        if not payload.text:
            raise ValueError("Empty request. Please provide a text.")

        normalized_text = normalize(payload.text)
        return StandardResponse(success=True, message="Text normalized successfully", data={"normalized_text": normalized_text})
    except ValueError as ve:
        return StandardResponse(success=False, message=str(ve), error_code=400)
    except HTTPException as he:
        return StandardResponse(success=False, message=str(he.detail), error_code=he.status_code)
    except Exception as e:
        return StandardResponse(success=False, message=str(e), error_code=500)

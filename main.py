from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_v1_router


app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix="/api/v1")

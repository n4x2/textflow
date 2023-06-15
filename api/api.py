from fastapi import APIRouter
from api.v1_endpoints import text

api_v1_router = APIRouter()
api_v1_router.include_router(text.router)

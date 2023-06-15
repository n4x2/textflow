from pydantic import BaseModel


class StandardResponse(BaseModel):
    success: bool
    message: str
    data: dict = {}
    error_code: int = None
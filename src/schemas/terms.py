from pydantic import BaseModel
from datetime import date


class TermCreate(BaseModel):
    name: str
    start_date: date
    end_date: date
    duration: str


class TermResponse(TermCreate):
    id: int
from pydantic import BaseModel
from datetime import date


class StudentCreate(BaseModel):
    name: str
    email: str
    gender: str
    company_name: str | None = None
    status: str | None = None
    term_id: int


class StudentResponse(StudentCreate):
    id: int
    enrolled_at: date
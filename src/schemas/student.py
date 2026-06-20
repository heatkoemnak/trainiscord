from pydantic import BaseModel
from datetime import date
from typing import Optional


class StudentBase(BaseModel):
    name: str
    email: str
    gender: Optional[str] = None
    company_name: Optional[str] = None
    status: Optional[str] = None
    enrolled_at: Optional[date] = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    company_name: Optional[str] = None
    status: Optional[str] = None
    enrolled_at: Optional[date] = None


class StudentOut(StudentBase):
    id: int

    class Config:
        from_attributes = True
from sqlalchemy import Column, Integer, String, Date
from src.config.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    gender = Column(String)
    company_name = Column(String)
    status = Column(String)
    enrolled_at = Column(Date)
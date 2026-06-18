from fastapi import APIRouter, Depends
from src.config.database import get_db
from src.services.student_service import StudentService
from src.schemas.student import StudentCreate

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/")
def get_students(db=Depends(get_db)):
    return StudentService.get_all(db)


@router.post("/")
def create_student(data: StudentCreate, db=Depends(get_db)):
    return StudentService.create(db, data)

@router.put("/{student_id}")
def update_student(student_id: int, data: StudentCreate, db=Depends(get_db)):
    return StudentService.update(db, student_id, data)
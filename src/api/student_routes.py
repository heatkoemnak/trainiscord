from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.config.database import SessionLocal
from src.schemas.student import StudentCreate, StudentUpdate, StudentOut
from src.services.student_service import StudentService

router = APIRouter(prefix="/students", tags=["Students"])


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[StudentOut])
def get_students(db: Session = Depends(get_db)):
    return StudentService.get_all(db)


@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = StudentService.get_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.post("/", response_model=StudentOut)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    return StudentService.create(db, data)


@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, data: StudentUpdate, db: Session = Depends(get_db)):
    student = StudentService.update(db, student_id, data)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    success = StudentService.delete(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}
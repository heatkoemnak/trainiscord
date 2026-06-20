from sqlalchemy.orm import Session
from src.models.student import Student
from src.schemas.student import StudentCreate, StudentUpdate


class StudentService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Student).all()

    @staticmethod
    def get_by_id(db: Session, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    @staticmethod
    def create(db: Session, data: StudentCreate):
        student = Student(**data.model_dump())
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    @staticmethod
    def update(db: Session, student_id: int, data: StudentUpdate):
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(student, key, value)

        db.commit()
        db.refresh(student)
        return student

    @staticmethod
    def delete(db: Session, student_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return False

        db.delete(student)
        db.commit()
        return True
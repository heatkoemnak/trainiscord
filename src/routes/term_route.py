from fastapi import APIRouter, Depends
from src.services.term_service import TermService
from src.config.database import get_db

router = APIRouter(prefix="/terms", tags=["Terms"])


@router.get("/")
def get_terms(db=Depends(get_db)):
    return TermService.get_all(db)

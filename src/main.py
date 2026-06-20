from fastapi import FastAPI
from src.api.student_routes import router as student_router
from src.config.database import engine, Base

app = FastAPI()

# create tables (for dev only)
Base.metadata.create_all(bind=engine)

app.include_router(student_router)


@app.get("/")
def root():
    return {"message": "API is running"}
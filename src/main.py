from fastapi import FastAPI
from src.config.database import get_db
from src.routes import student_route, term_route
app = FastAPI(
    title="Training API (Raw SQL)",
    version="1.0.0"
)

# Include routers
app.include_router(student_route.router)
app.include_router(term_route.router)


# Health check
@app.get("/")
def root():
    return {"message": "API is running 🚀"}


# Optional: create tables on startup (simple dev approach)
def startup():
    conn = next(get_db())

    with conn.cursor() as cur:
        # TERMS TABLE
        cur.execute("""
        CREATE TABLE IF NOT EXISTS terms (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            start_date DATE,
            end_date DATE,
            duration VARCHAR(100)
        );
        """)

        # STUDENTS TABLE
        cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            gender VARCHAR(10),
            company_name VARCHAR(100),
            status VARCHAR(50),
            enrolled_at DATE DEFAULT CURRENT_DATE,
            term_id INTEGER REFERENCES terms(id) ON DELETE SET NULL
        );
        """)

        conn.commit()
        conn.close()
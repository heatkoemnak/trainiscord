CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender VARCHAR(20),
    company_name VARCHAR(100),
    status VARCHAR(50),
    enrolled_at DATE DEFAULT CURRENT_DATE,
    term_id INTEGER REFERENCES terms(id)
);
"""
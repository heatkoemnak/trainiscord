from sqlalchemy import text
from src.config.database import get_db

db = get_db()

query = text("""
SELECT
    t.id,
    t.name,
    t.start_date,
    t.end_date,
    s.name AS student_name,
    s.company_name,
    s.gender
FROM student_terms st
JOIN terms t ON t.id = st.term_id
JOIN students s ON s.id = st.student_id
""")

result = db.execute(query)

for row in result:
    print(dict(row._mapping))
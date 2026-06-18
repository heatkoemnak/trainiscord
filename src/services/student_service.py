class StudentService:

    @staticmethod
    def get_all(conn):
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    s.id AS student_id,
                    s.name AS student_name,
                    s.email,
                    s.gender,
                    s.company_name,
                    s.status,
                    s.enrolled_at,

                    t.id AS term_id,
                    t.name AS term_name,
                    t.start_date,
                    t.end_date,
                    t.duration

                FROM students s
                LEFT JOIN terms t ON s.term_id = t.id
                ORDER BY s.id
            """)
            return cur.fetchall()
    @staticmethod
    def create(conn, data):
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO students
                (name,email,gender,company_name,status,term_id)
                VALUES (%s,%s,%s,%s,%s,%s)
                RETURNING *
            """, (
                data.name,
                data.email,
                data.gender,
                data.company_name,
                data.status,
                data.term_id
            ))

            conn.commit()
            return cur.fetchone()
        
    @staticmethod
    def update(conn, student_id: int, data):
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE students
                SET 
                    name = %s,
                    email = %s,
                    gender = %s,
                    company_name = %s,
                    status = %s,
                    term_id = %s
                WHERE id = %s
                RETURNING *
            """, (
                data.name,
                data.email,
                data.gender,
                data.company_name,
                data.status,
                data.term_id,
                student_id
            ))

            updated_student = cur.fetchone()
            conn.commit()

            return updated_student
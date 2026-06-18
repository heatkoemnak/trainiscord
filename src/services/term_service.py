class TermService:

    @staticmethod
    def get_all(conn):
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    t.id AS term_id,
                    t.name AS term_name,
                    t.start_date,
                    t.end_date,
                    t.duration,

                    s.id AS student_id,
                    s.name AS student_name,
                    s.email,
                    s.gender,
                    s.company_name,
                    s.status,
                    s.enrolled_at

                FROM terms t
                LEFT JOIN students s ON s.term_id = t.id
                ORDER BY t.id
            """)

            rows = cur.fetchall()

            terms_map = {}

            for row in rows:
                term_id = row["term_id"]

                if term_id not in terms_map:
                    terms_map[term_id] = {
                        "id": term_id,
                        "name": row["term_name"],
                        "start_date": row["start_date"],
                        "end_date": row["end_date"],
                        "duration": row["duration"],
                        "students": []
                    }

                if row["student_id"]:
                    terms_map[term_id]["students"].append({
                        "id": row["student_id"],
                        "name": row["student_name"],
                        "email": row["email"],
                        "gender": row["gender"],
                        "company_name": row["company_name"],
                        "status": row["status"],
                        "enrolled_at": row["enrolled_at"],
                    })

            return list(terms_map.values())
        
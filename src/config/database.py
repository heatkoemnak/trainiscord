import psycopg
from psycopg.rows import dict_row
from src.config.settings import settings


def get_db():
    conn = psycopg.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        row_factory=dict_row,
    )

    try:
        yield conn
    finally:
        conn.close()
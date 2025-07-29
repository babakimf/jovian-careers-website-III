import sqlalchemy 
from sqlalchemy import create_engine, text
import os

# Replace with your actual MySQL username, password, host, port, and database name
db_connection_string = os.getenv("DB_CONNECTION_STRING")
engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs
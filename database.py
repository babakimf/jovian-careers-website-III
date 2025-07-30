import sqlalchemy 
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


# Replace with your actual MySQL username, password, host, port, and database name
db_connection_string = os.getenv("DB_CONNECTION_STRING")
if not db_connection_string:
    raise ValueError("DB_CONNECTION_STRING environment variable is not set")
engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs 
    

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), 
                              {'val':id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:        
            return rows[0]._asdict()
        
# def add_application_to_db(job_id, data):
#     with engine.connect() as conn:
#         query = text("""INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
#                      VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)""")
#         result = conn.execute(query, 
#                               job_id = job_id, 
#                               full_name = data['full_name'], 
#                               email = data['email'], 
#                               linkedin_url = data['linkedin_url'], 
#                               education = data['education'], 
#                               work_experience = data['work_experience'],
#                               resume_url = data['resume_url'])
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("""INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
                     VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)""")
        conn.execute(query, {
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "linkedin_url": data['linkedin_url'],
            "education": data['education'],
            "work_experience": data['work_experience'],
            "resume_url": data['resume_url']
        })
        conn.commit() 

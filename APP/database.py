from sqlmodel import SQLModel,create_engine,Session,text
from dotenv import load_dotenv
import os

load_dotenv();
DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL,echo=True)

def test_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))     
        return True
    except Exception as e:
        print("Database connection failed:", e)
        return False

def create_db_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
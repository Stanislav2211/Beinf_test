from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.environ.get('USER_DB')
db_password = os.environ.get('PASSWORD_DB')
db_name = os.environ.get('NAME_DB')

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@127.0.0.1:5432/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
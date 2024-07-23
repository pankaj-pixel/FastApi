from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

print("THIS IS DATABASE : ",settings.DATABASE_NAME)
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}/{settings.DATABASE_NAME}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#data base connection for postgres implementation
"""while 1:
    try:
        conn = psycopg2.connect(host ='localhost', database = 'fastapi' , user ='postgres',password =123456,cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("connection Successfully")
        break

    except Exception as error:
        print("Failed Database connection")
        print("Error",error)
        time.sleep(2)
"""
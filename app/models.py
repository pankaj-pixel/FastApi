
from sqlalchemy import Column,Integer,String,Boolean
from app.Database import *
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Post(Base):
    __tablename__ ='post'
    id = Column(Integer,primary_key=True,nullable=False)
    Title =Column(String,nullable=False)
    content = Column(String,nullable=False)
    Published=Column(Boolean,server_default='TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


#cretae a model for user or login

class User(Base):
    __tablename__ ='users'
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
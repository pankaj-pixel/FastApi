
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
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
    #foreign key reference to id of users table
    owner_id = Column(Integer, ForeignKey('users.id',ondelete='CASCADE'),nullable=False)
    owner = relationship("User")



#Cretae a model for user or login 
class User(Base):
    __tablename__ ='users'
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class Vote(Base):
    __tablename__ ='votes'
    user_id = Column(Integer,ForeignKey("users.id",ondelete='CASCADE'),primary_key=True,nullable=False)    
    post_id = Column(Integer,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True,nullable=False)




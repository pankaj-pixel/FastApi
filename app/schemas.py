from pydantic import BaseModel,EmailStr
from datetime import datetime
from pydantic import conint

#user creating model
class User(BaseModel):
    email: EmailStr
    password:str


#after Creating User Response
class UserOut(BaseModel):
    id : int
    email: EmailStr
    created_at:datetime


class UserLogIn(BaseModel):
    email:EmailStr
    password : str




class PostBase(BaseModel):
    Title: str
    content:str
    Published :bool = True
    #created_at:datetime
    #create an optional field


#Inherting PostBase class in PostCreate
class PostCreate(PostBase):
    pass

#creating a Response model back to user
class PostResponse(PostBase):
    id:int
    Title: str
    content:str
    owner_id:int
    owner:UserOut


 
    #default Field
    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:str  

class votes(BaseModel):
    post_id:int
    dir:int  
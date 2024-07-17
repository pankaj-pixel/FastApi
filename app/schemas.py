from pydantic import BaseModel,EmailStr
from datetime import datetime

   

class PostBase(BaseModel):
    Title: str
    content:str
    #default Field
    Published :bool = True
    #create an optional field

#inherting PostBase class in PostCreate
class PostCreate(PostBase):
    pass

#creating a Response model back to user
class PostResponse(PostBase):
    id:int
    Title: str
    content:str
    created_at:datetime
    #default Field
    class Config:
        orm_mode = True


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

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:str   
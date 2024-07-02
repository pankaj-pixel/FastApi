from fastapi import FastAPI
from fastapi.params import Body
#To cretae data schemas we uses pydantic
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#create a class for post of post data
class post(BaseModel):
    Title: str
    content:str
    #default Field
    Published :bool = True
    #create an optional field
    Ratings :Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


"""@app.post("/posts")
async def get_post(payload: dict = Body()):
    print(payload)
    return {f"Title : {payload['Title'] } Content : {payload['content'] }"}"""

#which model schema 
@app.post("/posts")
def create_post(payload:post):
    print(payload)
    print(payload.Title)
    print(payload.content)
    print(payload.Ratings)
    return {"data : New Post Created"}
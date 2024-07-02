from fastapi import FastAPI
from fastapi.params import Body

#to cretae data schemas we uses pydantic
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/posts")
async def get_post(payload: dict = Body()):
    print(payload)
    return {f"Title : {payload['Title'] } Content : {payload['content'] }"}

@app.post("/posts")
def create_post():
    return {"data : New Post Created"}
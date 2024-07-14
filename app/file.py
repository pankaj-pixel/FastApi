from fastapi import FastAPI,status,Depends
from fastapi import status
from fastapi.params import Body
#To cretae data schemas we uses pydantic
from pydantic import BaseModel
from typing import Optional,List
import random
from fastapi.exceptions import HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
#from Database import engine,get_db
import time

from sqlalchemy.orm import Session
from .Database import SessionLocal, engine,get_db
from .import models,schemas,utils

app = FastAPI()



models.Base.metadata.create_all(bind=engine)



#data base connection for postgres implementation
while 1:
    try:
        conn = psycopg2.connect(host ='localhost', database = 'fastapi' , user ='postgres',password =123456,cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("connection Successfully")
        break

    except Exception as error:
        print("Failed Database connection")
        print("Error",error)
        time.sleep(2)




# bprint(my_posts)
#create a class for post of post data
class Post(BaseModel):
    Title: str
    content:str
    #default Field
    Published :bool = True
    #create an optional field
    Ratings :Optional[int] = None


#get query with sqlalchemy
@app.get("/",response_model=List[schemas.PostResponse])
def test_posts(db:Session = Depends(get_db)):
     posts = db.query(models.Post).all()
     print(posts)
     return posts


# get post with regular sql
#@app.get("/")
#async def root():
#    cursor.execute("""SELECT * FROM post """)
#    postdata = cursor.fetchall()
#    print(postdata)
#    return postdata



"""@app.post("/posts")
async def get_post(payload: dict = Body()):
    print(payload)
    return {f"Title : {payload['Title'] } Content : {payload['content'] }"}

#Reterive all posts 
@app.post("/posts")

def create_post(post:Post):
    print(post)
    #print(payload.Title)
    #print(payload.content)
    #print(payload.Ratings) 
    print(post.dict())"""
    #return {"data : New Post Created"}"""



"""
@app.post("/posts")
def create_post(post:Post):
    avail_posts = post.dict()
    print(avail_posts)
    avail_posts['id'] = random.randrange(0,1234556)
    my_posts.append(avail_posts)
    print(my_posts)
    return {f"data :{avail_posts}"}
"""
#create post using sqlalchemy
@app.post("/Create_posts",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_post(post:schemas.PostCreate,db:Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) 
    return new_post
   

     

#create post using Raw sql
#@app.post("/Create_posts",status_code=status.HTTP_201_CREATED)
#def create_post(post:Post):
#     cursor.execute(""" INSERT INTO post("Title",content,"Published" ) VALUES (%s,%s,%s) RETURNING
#                    * """,(post.Title,post.content,post.Published))
#     newpost = cursor.fetchone()
#     conn.commit()
#     return {"data":newpost}



#get the latest post added
"""@app.get("/post/latest")
def get_the_latest_post():
    post = my_posts[len(my_posts)-1]
    print(post)
    return post
"""


#get post by id 
"""@app.get("/posts/{id}",status_code=status.HTTP_201_CREATED)
def retrieve_post_by_id(id:int):
    for post in my_posts:
        print(post)
        if post["id"] == id:
            print(post["id"])
            return post
        if not post:
            return { status.HTTP_404_NOT_FOUND }
    # If the loop completes without finding the post, raise HTTPException with 404 Not Found
    raise HTTPException(status_code = 404, detail="Post not found")

"""






#get post by id using database
#@app.get("/posts/{id}",status_code=status.HTTP_200_OK)
#def retrieve_post_by_id(id:int):
#        cursor.execute("""SELECT *  FROM public.post WHERE id = %s """,(str(id),))
#        id_data = cursor.fetchone()
#        print(id_data)
#        # Check if id_data is None (no data found)
#        if id_data is None:
#            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post found with id {id}")
#        Return the fetched data
#        return id_data




#get post by id using SQLALCHEMY
@app.get("/posts/{id}",status_code=status.HTTP_200_OK)
def retrieve_post_by_id(id:int,db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    #print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post found with id {id}")
    return  post






#Delete post by id using sqlAlchemy
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_postby_id(id:int,db:Session = Depends(get_db)): 
        post = db.query(models.Post).filter(models.Post.id == id)
        if not post.first():
             return HTTPException(status_code=404,detail= f"Post {id} Doesnot Exist")
        post.delete(synchronize_session=False)
        db.commit()
        return {"message": f"Post with id {id} has been successfully deleted"}
    








#Delete post by id 
#@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
#def delete_postby_id(id:int): 
#        cursor.execute("""DELETE FROM post WHERE id = %s """,(str(id),))
#        conn.commit()
#        if not id:
#             return HTTPException(status_code=404,detail= f"Post {id} Doesnot Exist")
#        return {"message": f"Post with id {id} has been successfully deleted"}
    


#update post
"""@app.put("/posts/{id}",status_code=204)
def update_request(id:int,post:Post):
    index = Find_index(id)
    if index == None:
        return HTTPException(status_code=404,detail="Post Doesnot Exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {f"data : {my_posts}"}

"""



#update post in database through api
@app.put("/update_posts/{id}",response_model=schemas.PostResponse)
def update_request(id:int,post:schemas.PostBase,db:Session = Depends(get_db)):
    updated_post = db.query(models.Post).filter(models.Post.id == id).first()
    
    # Check if the post with the given id exists
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    
    # Update the post with the new data
    for field in post.dict(exclude_unset=True):
        setattr(updated_post, field, getattr(post, field))
    
    # Commit the changes to the database
    db.commit()
    
    return updated_post



#update post in database through api
#@app.put("/update_posts/{id}",status_code=204)
#def update_request(id:int,post:Post):
#    cursor.execute("""UPDATE public.post SET "Title" = %s ,content =%s ,"Published" = %s WHERE id = %s RETURNING * """,(post.Title, post.content, post.Published ,str(id)))
#    updatespost = cursor.fetchone()
#    conn.commit()

#    if updatespost == None:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id Not Found !!!") 
#    return{"Data ": updatespost}




#working on User Model 
@app.post("/CreateUser",response_model=schemas.UserOut)
def create_post(user:schemas.User,db:Session = Depends(get_db)):
    
    #hashing the password
    hased = utils.hash(user.password)
    user.password = hased
    newUser = models.User(**user.dict())  
    db.add(newUser)
    db.commit()
    db.refresh(newUser) 
    return newUser
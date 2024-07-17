from fastapi import FastAPI,status,Depends,Response,HTTPException,APIRouter
from sqlalchemy.orm import Session
from .. import models ,schemas
from ..routes import oauth
from ..Database import get_db
from psycopg2.extras import RealDictCursor
from typing import List

router = APIRouter()


#get query with sqlalchemy
@router.get("/",response_model=List[schemas.PostResponse])
def test_posts(db:Session = Depends(get_db),user_id:int =Depends(oauth.get_current_user)):
     posts = db.query(models.Post).all()
     print(posts)
     return posts


#get post by id using SQLALCHEMY
@router.get("/posts/{id}",status_code=status.HTTP_200_OK)
def retrieve_post_by_id(id:int,db:Session = Depends(get_db),user_id:int =Depends(oauth.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    #print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post found with id {id}")
    return  post


 #post using sqlalchemy
@router.post("/Create_posts",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_post(post:schemas.PostCreate,db:Session = Depends(get_db),user_id:int =Depends(oauth.get_current_user)):
    print(user_id)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) 
    return new_post
   





#Delete post by id using sqlAlchemy
@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_postby_id(id:int,db:Session = Depends(get_db),user_id:int =Depends(oauth.get_current_user)): 
        post = db.query(models.Post).filter(models.Post.id == id)
        if not post.first():
             return HTTPException(status_code=404,detail= f"Post {id} Doesnot Exist")
        post.delete(synchronize_session=False)
        db.commit()
        return {"message": f"Post with id {id} has been successfully deleted"}
    




#update post in database through api
@router.put("/update_posts/{id}",response_model=schemas.PostResponse)
def update_request(id:int,post:schemas.PostBase,db:Session = Depends(get_db),user_id:int =Depends(oauth.get_current_user)):
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
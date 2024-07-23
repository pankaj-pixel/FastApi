from fastapi import FastAPI,status,Depends,Response,HTTPException,APIRouter
from ..import schemas
from ..import Database
from sqlalchemy.orm import Session
from .import oauth
from ..import models


router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)
@router.post("/")
def vote(vote:schemas.votes,db:Session = Depends(Database.get_db),current_user:int =Depends(oauth.get_current_user)):
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id , models.Vote.user_id == current_user)
    found_post = vote_query.first()

    #if vote.dir ==1 that means user want to create a post
    if vote.dir ==1:
        if found_post:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user {current_user} has already Exists")
         
        new_vote = models.Vote(post_id = vote.post_id,user_id = current_user)
        db.add(new_vote)
        db.commit()
        return{"message : new Vote created successfully"}  
    else:
        if not found_post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return{"message : Successfully Deleted Message"}

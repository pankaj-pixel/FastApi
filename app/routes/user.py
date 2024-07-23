from fastapi import FastAPI,status,Depends,Response,HTTPException,APIRouter
from .. import models ,schemas,utils
from ..Database import SessionLocal, engine,get_db
from sqlalchemy.orm import Session
from typing import Optional,List


router = APIRouter()


@router.post("/CreateUser",response_model=schemas.UserOut)
def create_post(user:schemas.User,db:Session = Depends(get_db)):
    try:

        hased = utils.hash(user.password)
        user.password = hased
        newUser = models.User(**user.dict())  
        db.add(newUser)
        db.commit()
        db.refresh(newUser) 
        return newUser
    except PermissionError as e:
        print(e)

#fetching users information by id
@router.get("/user/{id}",response_model=schemas.UserOut)
def get_user(id: int ,db:Session = Depends(get_db),):
    user = db.query(models.User).filter(models.User.id ==id).first()
    if not id :
       return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=" id Not Found !!!") 
    return user


#fetching users information by id
@router.get("/allusers", response_model=List[schemas.UserOut])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    print("userIn : ",users)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users

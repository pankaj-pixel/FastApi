from fastapi import FastAPI,status,Depends,APIRouter,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..import Database ,schemas,utils,models
from .import oauth

router = APIRouter()


"""@router.post("/login")
def login_in(user_credentials: schemas.UserLogIn, db: Session = Depends(Database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email and models.User.password == user_credentials.password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    access_token = oauth.create_access_token(data ={"user_id": user.id})
    return {"access_token":access_token,"Token_Type":"Bearer Token"}
"""

# dded form data as input email/username and password.
@router.post("/login")
def login_in(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(Database.get_db)):
    print(schemas.Token)
    user = db.query(models.User).filter(models.User.email == user_credentials.username and models.User.password == user_credentials.password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    #  Adding user_id inside token as data we can add any number of data init.
    access_token = oauth.create_access_token(data ={"user_id": user.id})
    return {"access_token":access_token,"Token_Type":"Bearer Token"}
from datetime import datetime, timedelta, timezone
from jose import JWTError,jwt
from ..import schemas
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from ..config import settings

ALGORITHM =settings.ALGORITHM
SECRET_KEY = settings.SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

#create the token and embeede expire date,sceret key and algorithm
def create_access_token(data:dict ,expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) +  timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    print(expire)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    print(encode_jwt)
    return encode_jwt

def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get('user_id')
        if not id:
            raise credentials_exception
        token_data = schemas.TokenData.id=id

        return token_data
    except JWTError:
        raise credentials_exception  
        


def get_current_user(token:str =Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",headers={"www-Authenticate":"Bearer"})
    verify_token(token, credentials_exception)
    return  verify_token(token,credentials_exception)
    
     



    

    
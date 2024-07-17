from datetime import datetime,timedelta
from jose import JWTError,jwt
from ..import schemas
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
ALGORITHM ="HS256"
SECRET_KEY = "aewsfmorjo23j4j4oi2n3nr23noin24ioh5oi34t3bti43ntiohntgio"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

#create the token and embeede expire date,sceret key and algorithm
def create_access_token(data:dict ,expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    print(expire)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    print(encode_jwt)
    return encode_jwt


def verify_token(Token:str,credentials_exception):
    try:
        payload = jwt.decode(Token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get('user_id')
        if not id:
            raise credentials_exception
        token_data = schemas.TokenData.id=id
        return token_data
    except JWTError:
        raise credentials_exception  
         


def get_current_user(token:str =Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",headers={"www-Authenticate":"Bearer"})
    return verify_token(token,credentials_exception)
     


    

    
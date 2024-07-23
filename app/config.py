from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOSTNAME:str
    DATABASE_NAME : str 
    DATABASE_PORT : str
    DATABASE_PASSWORD : str
    DATABASE_USERNAME : str
    DATABASE_NAME : str
    ALGORITHM :str
    SECRET_KEY : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
     
    class Config:
        env_file =".env" 

settings = Settings()
from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional , Literal
from pydantic.types import conint

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    
    class Config:
        orm_mode = True
    
class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    
class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserOut
    
    class Config:
        orm_mode = True
        
class PostOut(BaseModel):
    Post : Post
    votes : int
    
    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id : int
    dir: Literal[0,1]
    
class Token(BaseModel):
    access_token = str
    token_type = str
    
class TokenData(BaseModel):
    id : Optional[str]=None

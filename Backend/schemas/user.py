from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


##validation stuffing [registration]
class UserCreate(BaseModel):
    username :str  = Field(...,min_length=3, max_length=25)
    full_name : Optional[str] =  None
    email : EmailStr
    password : str
    biography : Optional[str] = None
    nationality: Optional[str]
    profile_pic : Optional[str] = None
    gender: Optional[str]  = None
    role_id: Optional[int] = None
    fav_food: Optional[str] = None

#sends output to client
class UserOut(BaseModel):
    id: int
    username: str 
    full_name: Optional[str]
    email: EmailStr
    biography : Optional[str] 
    profile_pic : Optional[str] 
    nationality: Optional[str]
    gender: Optional[str] 
    is_verified: bool
    role_id: Optional[int]
    joined_date: datetime

    model_config  ={
        "from_attributes": True
    }



#login request
class loginFormat(BaseModel):
    username : str
    password: str


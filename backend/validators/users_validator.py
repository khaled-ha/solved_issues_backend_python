from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Union


class UserBase(BaseModel):
    email: EmailStr
    password: str
    is_verified: bool = False
    name: str
    photo: str
    role: Union[str, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id
    int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class RegistrationUserResponse(BaseModel):
    message: str
    # data : UserResponse


class NotFoundResponse(BaseModel):
    message: str
    # data : UserResponse

from datetime import date

from typing import List
from pydantic import BaseModel, EmailStr
from typing import Union

from typing import Optional


class Token(BaseModel):
    accessToken: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr


class payload(BaseModel):
    email: EmailStr
    role: str
    phone: str
    name: str
    userName: str
    image: str

    class Config:
        orm_mode = True


class SignUp(BaseModel):
    email: EmailStr
    password: str
    firstName: str
    lastName: str
    role: str
    phone: str

    class Config:
        orm_mode = True

class SignUpOut(BaseModel):
    email: EmailStr
    firstName: str
    lastName: str
    role: str
    phone: str
    userName: str
    status: str

    class Config:
        orm_mode = True
    
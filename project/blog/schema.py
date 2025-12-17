from pydantic import BaseModel


class blog(BaseModel):
    title: str
    body: str
    
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str      


class showuser(BaseModel):
    name: str
    email: str
    blogs: list[blog] = []

    class Config:
        orm_mode = True

class show_blog(BaseModel): 
    title: str
    body: str
    creator : showuser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str 

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel): 
    email: str | None = None
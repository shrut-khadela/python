from sqlalchemy.orm import Session
from fastapi import  Depends , status , HTTPException
from project.blog import schema , models , hashing

def creat_user(request: schema.User, db:Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.hash.hash_password(request.password))
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail=f"User of id:{id} is  not found")
    return user


def update(id:int, request: schema.User, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail=f"User of id:{id} is  not found")
    user.update({"name": request.name, "email": request.email, "password":hashing.hash.hash_password(request.password)})
    db.commit()
    return "User has been updated"
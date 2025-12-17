from sqlalchemy.orm import Session
from project.blog import models , database , schema 
from fastapi import HTTPException , status , Response
def all_blogs(db:Session):
    blogs = db.query(models.blog).all()  
    return blogs 

def create_blog(request: schema.blog, db:Session):
    new_blog = models.blog(title=request.title, body=request.body, user_id=1 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id:int, db:Session):
    blog = db.query(models.blog).filter(models.blog.id == id)
    if not blog.first():
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog of id:{id} is  not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return f"Blog with id {id} has been deleted"

def update_blog(id:int, request: schema.blog, db:Session):
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog of id:{id} is  not found")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return "Blog has been updated"

def show_blog(id:int, db:Session):
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog of id:{id} is  not found")
    return blog


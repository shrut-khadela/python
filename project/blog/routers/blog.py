from sqlalchemy.orm import Session 
from fastapi import APIRouter , Depends , status , HTTPException ,   Response
from project.blog import schema , database , oauth2
from project.blog.repository import blog 


router = APIRouter(
    prefix = "/blog",
    tags=["Blogs"]
    ) 

get_db = database.get_db


@router.get("/",response_model=list[schema.show_blog])
def all(db:Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.all_blogs(db)


@router.post("/",status_code=status.HTTP_201_CREATED)
def create_blog(request: schema.blog,db:Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db:Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schema.blog, db:Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id ,request ,db)


@router.get("/{id}",status_code=200,response_model=schema.show_blog) 
def show(id, db:Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)   ):
    return blog.show_blog(id, db)


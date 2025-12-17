from sqlalchemy.orm import Session
from fastapi import APIRouter , Depends , status , HTTPException
from project.blog import schema , database , models , hashing 
from project.blog.repository import user

router = APIRouter(
    prefix = "/user",
    tags=["Users"]
        )

get_db = database.get_db

@router.post("/",response_model=schema.showuser)
def create_user(request: schema.User, db:Session = Depends(get_db)):
    return user.creat_user(request, db)


@router.get("/{id}",response_model=schema.showuser)
def show(id, db:Session = Depends(get_db)):
    return user.show(id, db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_user(id, request: schema.User, db:Session = Depends(get_db)):
    return user.update(id ,request ,db)
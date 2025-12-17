
from fastapi import APIRouter , Depends , HTTPException , status
from project.blog import schema , database , models , token
from sqlalchemy.orm import Session
from project.blog.hashing import hash
from fastapi.security import OAuth2PasswordRequestForm 

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Invalid Username")
    if not hash.verify(request.password , user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Invalid Password")
    
    access_token = token.create_access_token(data={"sub": user.email })
    return schema.Token(access_token=access_token, token_type="bearer")


print("Authenticate Router Loaded")
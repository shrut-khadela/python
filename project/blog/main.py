from fastapi import FastAPI
from project.blog import models
from project.blog.database import engine
from project.blog.routers import blog , user , authenticate



app = FastAPI() 

models.blog.metadata.create_all(bind=engine)

app.include_router(blog.router) 
app.include_router(user.router)
app.include_router(authenticate. router)











# def get_db():
#     db = sessionlocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/blog",status_code=status.HTTP_201_CREATED,tags=["Blogs"])
# def create_blog(request: schema.blog,db:Session = Depends(get_db)):
#     new_blog = models.blog(title=request.title, body=request.body, user_id=1 )
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog   

# @app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
# def delete_blog(id, db:Session = Depends(get_db)):
#     blog = db.query(models.blog).filter(models.blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return f"Blog with id {id} has been deleted"

# @app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
# def update_blog(id, request: schema.blog, db:Session = Depends(get_db)):
#     db.query(models.blog).filter(models.blog.id == id).update({"title": request.title, "body": request.body})
#     db.commit() 
#     return "Blog has been updated"

# # @app.get("/blog",response_model=list[schema.show_blog],tags=["Blogs"])
# # def all(db:Session = Depends(get_db)):
# #     blogs = db.query(models.blog).all()
# #     return blogs 

# @app.get("/blog/{id}",status_code=200,response_model=schema.show_blog,tags=["Blogs"]) 
# def show(id,responce:Response, db:Session = Depends(get_db)):
#     blog = db.query(models.blog).filter(models.blog.id == id).first()
#     if not blog:
#         raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog of id:{id} is  not found")
#         # responce.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail": f"Blog of id:{id} is  not found"}
#     return blog 


#  User Creation with Password Hashing


# @app.post("/user",response_model=schema.showuser,tags=["Users"])
# def create_user(request: schema.User, db:Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password=hashing.hash.hash_password(request.password))
#     db.add(new_user) 
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/user/{id}",response_model=schema.showuser,tags=["Users"])
# def show(id, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail=f"User of id:{id} is  not found")
#     return user
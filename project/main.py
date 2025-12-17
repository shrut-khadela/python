from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/demo")
def demo():
    A = "This is a demo FastAPI application."
    print(A)
    return {
    "message": "Hello World",
    "A": A,
    "data": {"name": "shrut"}
}

@app.get("/blog/unpublished")
def about():
    return {"data": " all unpublished blogs"}

@app.get("/blog/{id}")
def about(id: int ):
    return {"id" : id }

@app.get("/blog")
def blog(limit, published: bool):
    if published:
        return {"data": f"all published blogs with limit {limit}"}
    else:
        return {"data": f"all blogs with limit {limit}"}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/post")
def creat_blog (blog:Blog):
    return {"data": f"blog is created with title {blog.title}"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=2703)
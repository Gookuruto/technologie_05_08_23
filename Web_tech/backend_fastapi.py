from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Blog(BaseModel):
    title: str
    content: str

blogs = []

@app.post("/blogs", response_model=Blog)
def create_blog(blog: Blog):
    blogs.append(blog)
    return blog

@app.get("/blogs", response_model=List[Blog])
def get_blogs():
    return blogs

@app.get("/blogs/{blog_id}", response_model=Blog)
def get_blog(blog_id: int):
    if blog_id < 0 or blog_id >= len(blogs):
        raise HTTPException(status_code=404, detail="Blog not found")
    return blogs[blog_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

from pydantic import BaseModel



class Post(BaseModel):
    title: str
    content: str

class Comment(BaseModel):
    comment: str
    user_id: int
    post_id: int

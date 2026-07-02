from fastapi import FastAPI
from . import schemas , database # Present in same Root Folder
from typing import Optional

app = FastAPI()

@app.get("/")
def Home_Page():
    """This is the Home Page Without any Parameters"""
    return {"Message": "Welcome to Home Page ."}

@app.get("/posts")
def see_all_posts(limit: int = 10, skip: int = 0, id: Optional[int] = None, title: Optional[str] = None, content: Optional[str] = None):
    """
    limit - number of posts to return
    skip - number of posts to skip
    id - post id
    title - post title
    content - post content
    """
    filtered_posts = database.my_posts
    
    if id is not None:
        if id <= 0:
            return {"Error": "id less than or equal to 0 is invalid."}
        filtered_posts = [p for p in filtered_posts if p["id"] == id]

    if title:
        filtered_posts = [p for p in filtered_posts if title.lower() in p["title"].lower()]

    if content:
        filtered_posts = [p for p in filtered_posts if content.lower() in p["content"].lower()]

    if filtered_posts:
        return filtered_posts[skip : skip + limit]
        
    return {"Error": "Post not Found"}

@app.get("/posts/{id}")
def see_post_by_id(id: int):
    """
    Returning a single post of the provided id 
    """
    for p in database.my_posts:
        if p["id"] == id:
            return p
            
    return {"Error": "Post Not Found"} 

@app.post("/create_post")
def create_post(post: schemas.Post):
    """
    Create New Post
    """
    # Use the Pydantic model to receive a JSON body
    new_id = len(database.my_posts) + 1
    
    # Convert Pydantic model to dictionary
    new_post = post.dict()
    new_post["id"] = new_id
    
    database.my_posts.append(new_post)
    return {"message": "Post Created Successfully.", "post": new_post}

@app.put("/posts/{id}")
def update_post(id: int, post: schemas.Post):
    """
    Update an existing post
    """
    for index, p in enumerate(database.my_posts):
        if p["id"] == id:
            # Create a new dictionary with the updated data but keep the same ID
            updated_post = post.dict()
            updated_post["id"] = id
            
            # Replace the old post in the list with the new one
            database.my_posts[index] = updated_post
            return {"message": "Post updated successfully", "post": updated_post}
            
    return {"Error": "Post not found"}

@app.delete("/posts/{id}")
def delete_post(id: int):
    """
    Delete a specific post
    """
    for index, p in enumerate(database.my_posts):
        if p["id"] == id:
            # Remove it from the list
            deleted_post = database.my_posts.pop(index)
            return {"message": "Post deleted successfully", "deleted_post": deleted_post}
            
    return {"Error": "Post not found"}

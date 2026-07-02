# 🚀 My First FastAPI Practice Project

Hey! Welcome to my practice API project. I built this completely from scratch to learn how backend APIs work using Python and FastAPI. 

It's not connected to a real database yet (we'll get there!), but it works perfectly as a fully functional in-memory CRUD application.

## 🧠 What I Learned (The Journey)
I started with everything crammed into a single `main.py` file, but I learned a ton along the way:

- **Path vs. Query Parameters:** I figured out how to extract data straight from the URL path (like `/posts/5`) and how to use Query Parameters (like `?limit=10&title=pizza`) to filter data.
- **Advanced Filtering:** I learned how to stack list comprehensions to create powerful filters instead of trying to use `.append()` to search. 
- **Pagination:** I built `limit` and `skip` directly into my GET requests.
- **Pydantic Models:** I learned how to define the exact shape of my data using Pydantic, making sure users can't send bad data when creating a post.
- **Professional Project Structure:** I refactored my messy single file into a proper modular app! I split my code into `main.py` (for routing), `schemas.py` (for models), and `database.py` (for my fake data list).

## 😅 Mistakes I Made (And Fixed!)
You can't learn without breaking things. Here are a few things that tripped me up, but I managed to conquer:
1. **The `=` vs `:` Trap:** I accidentally used equals signs (`id = int`) instead of colons (`id: int`) when building my Pydantic models. 
2. **The `Optional` Syntax:** I tried doing `Optional(default=None)` instead of the correct `Optional[int] = None`.
3. **Using GET logic in POST requests:** I tried creating a new post by putting the data in the URL as query parameters, before realizing that POST requests are supposed to securely send data in the **Body** (as JSON).
4. **Logic Bugs:** I accidentally put a `return` error statement right in the middle of my function body without a proper `if` condition, which broke the whole endpoint! But I quickly learned how to nest my checks.

## ✨ What I Did Best
My logical instincts were spot on! Even when I didn't know the exact Python syntax, I knew exactly *what* the code was supposed to do. 
- I knew I needed a data model to structure my data.
- I correctly figured out the logic to auto-generate a new ID without a database (`len(my_posts) + 1`).
- I successfully tackled combining multiple query parameters (`id`, `title`, `content`) into a single endpoint, which is something a lot of beginners are afraid to try.

## 🛠️ Features (Fully Functional CRUD!)
- `GET /` - Welcome Page
- `GET /posts` - Get all posts (Supports filtering by `id`, `title`, `content` and pagination with `limit`/`skip`)
- `GET /posts/{id}` - Get a single post
- `POST /create_post` - Create a new post (using JSON body)
- `PUT /posts/{id}` - Update an existing post
- `DELETE /posts/{id}` - Delete a post

## 🏃 How to run this
1. Make sure you have the required libraries installed.
2. Run this command from the root folder: 
   ```bash
   uvicorn app.main:app --reload
   ```
3. Open `http://127.0.0.1:8000/docs` to test the API!

This is just the beginning. Next stop: real databases and user authentication!

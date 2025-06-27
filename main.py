import os
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Supabase setup
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Supabase URL and Key must be set in the environment variables.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# Pydantic model for the 'users' table
class User(BaseModel):
    id: int
    name: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Supabase FastAPI Vercel Example!"}

@app.get("/items", response_model=List[User])
async def get_items():
    """
    Retrieve all users from the 'users' table.
    """
    try:
        response = supabase.table("users").select("id, name").execute()
        
        # Check if the response has data
        if not response.data:
            return []

        # Convert data to list of User models
        users = [User(**item) for item in response.data]
        return users
    except Exception as e:
        print(f"Error fetching items from Supabase: {e}") # Log error for debugging
        # In a production app, you might want to return a more specific error
        # or handle different types of exceptions (e.g., network errors, Supabase errors)
        raise HTTPException(status_code=500, detail=f"Failed to retrieve items from database: {str(e)}")

# To run locally (optional, as Vercel handles this):
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
app = app
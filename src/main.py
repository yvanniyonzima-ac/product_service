import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env (like dotenv() in Rust)
load_dotenv()

# Get the port from environment or use default (3030)
PORT = int(os.getenv("PORT", 3030))

# Create a FastAPI instance
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) to allow requests from any domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Restrict to GET requests
    allow_headers=["*"],  # Allow all headers
)

# Define the "/products" route
@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:3001",
    "localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = [
    {
        "id": 1,
        "item": "Buy milk",
    },
    {
        "id": 2,
        "item": "Buy bread",
    },
    {
        "id": 3,
        "item": "Buy cheese",
    }
]
@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to this fantastic app!"}

@app.get("/todo", tags=["Todos"])
async def get_todos() -> dict:
    return {"data": todos}
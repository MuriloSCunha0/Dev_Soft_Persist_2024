from fastapi import FastAPI
from model import Book, User, Rating



app = FastAPI()

@app.post("/root")
def root():
    return {"IDLE"}
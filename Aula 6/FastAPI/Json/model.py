from pydantic import BaseModel

class Book(BaseModel):
    id_book: int
    title: str
    author: str
    year: int
    price: float
    pages: int
    gender: str

class User(BaseModel):
    id_user: int
    name: str
    city: str
    age: int

class Rating(BaseModel):
    id_user: int
    id_book: int
    rating: float
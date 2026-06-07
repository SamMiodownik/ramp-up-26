from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int

app = FastAPI()

books = []

next_id = 1

@app.post("/books/")
def create(book: Book):
    global next_id

    new_book = {
        "id" : next_id,
        "title" : book.title,
        "author" : book.author,
        "year" : book.year
    }

    books.append(new_book)

    next_id += 1

    return new_book

@app.get("/books/")
def get_books():
    return books

@app.get(f"/books/{id}")
def get_book_by_id(id : int):
    for book in books:
        if book["id"] == id:
            return book   

    raise HTTPException(status_code = 404, detail = "Book not found")


@app.put(f"/books/{id}")
def update(id : int, updated_book : Book):
    for book in books:
        if book["id"] == id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["year"] = updated_book.year

            return book
        
    raise HTTPException(status_code = 404, detail = "Book not found")

@app.delete(f"/books/{id}")
def delete(id : int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"detail": "Book deleted successfully"}
        
    raise HTTPException(status_code = 404, detail = "Book not found")
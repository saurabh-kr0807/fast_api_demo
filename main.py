from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from methods import create_book, create_review, get_books, get_reviews, update_book,delete_book, update_review, delete_review
from database import SessionLocal,engine
from models import Base
from serializers import BookCreate, BookResponse, ReviewCreate, ReviewResponse
from typing import List

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# db connection call during thr run of the application
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# book post call to add the new book
@app.post("/books/", response_model=BookCreate)
async def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, title=book.title, author=book.author, publication_year=book.publication_year)

# book get call to get the book details using Author and Publication Year filter
@app.get("/books/", response_model=List[BookResponse])
async def get_books_endpoint(author: str = Query(None, title="Author"),
                             publication_year: int = Query(None, title="Publication Year"),
                             db: Session = Depends(get_db)):
    return get_books(db, author=author, publication_year=publication_year)

# book update call for update the book information
@app.put("/books/{book_id}", response_model=BookResponse)
async def update_books_endpoint(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    return update_book(db, book_id=book_id, title=book.title, author=book.author, publication_year=book.publication_year)

# book delete call for delete the book information
@app.delete("/books/{book_id}", response_model=str)
async def delete_books_endpoint(book_id: int, db: Session = Depends(get_db)):
    return delete_book(db, book_id=book_id)

# review post call to add the review for a book
@app.post("/reviews/", response_model=ReviewCreate)
async def create_review_endpoint(review:ReviewCreate, db: Session = Depends(get_db)):
    return create_review(db, text=review.text, rating=review.rating, book_id=review.book_id)

# review get call to get the review on the basis of book
@app.get("/reviews/{book_id}", response_model=list[ReviewResponse])
async def get_reviews_endpoint(book_id: int, db: Session = Depends(get_db)):
    reviews = get_reviews(db, book_id)
    if reviews is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return reviews

# review update call to update the review of the any book
@app.put("/reviews/{review_id}", response_model=ReviewCreate)
async def update_reviews_endpoint(review_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    return update_review(db, review_id=review_id, text=review.text, rating=review.rating, book_id=review.book_id)

# review delete call to delete the review of the any book
@app.delete("/reviews/{review_id}", response_model=str)
async def delete_reviews_endpoint(review_id: int, db: Session = Depends(get_db)):
    return delete_review(db, review_id=review_id)
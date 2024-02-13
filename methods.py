from sqlalchemy.orm import Session
from models import Book, Review
from fastapi import HTTPException


def create_book(db: Session, title: str, author: str, publication_year: int):
    """ Create the New Book information and saving in DB return the same information

    :param db: Session
    :param title: str
    :param author: str
    :param publication_year: int
    :return: Book
    """
    book = Book(title=title, author=author, publication_year=publication_year)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def create_review(db: Session, text: str, rating: int, book_id: int):
    """ Create a review for a book and saving in DB return the same information

    :param db: Session
    :param text: str
    :param rating: int
    :param book_id: int
    :return: Review
    """
    review = Review(text=text, rating=rating, book_id=book_id)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

def get_books(db: Session, author: str = None, publication_year: int = None):
    """ Get the Book information with author and publication_year filter and return the Book list

    :param db: Session
    :param author: str
    :param publication_year: int
    :return: Book list
    """
    books = db.query(Book).filter(
        (Book.author == author) if author else True,
        (Book.publication_year == publication_year) if publication_year else True
    ).all()
    return books

def get_reviews(db: Session, book_id: int):
    """ Get the review for a book

    :param db: Session
    :param book_id: int
    :return: Review
    """
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        return None
    return book.reviews


def update_book(db: Session, book_id: int, title: str, author: str, publication_year: int):
    """ Update the Book information with the book_id and return the same information

    :param db: Session
    :param book_id: int
    :param title: str
    :param author: str
    :param publication_year: int
    :return: Book
    """
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = title
    db_book.author = author
    db_book.publication_year = publication_year
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    """ Delete the Book information from DB with book_id

    :param db: Session
    :param book_id: int
    :return: str
    """
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return "Book deleted successfully"

def update_review(db: Session, review_id: int, text: str, rating: int, book_id: int):
    """ Update the review for the book and return the same information

    :param db: Session
    :param review_id: int
    :param text: str
    :param rating: int
    :param book_id: int
    :return: Review
    """
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    db_review.text = text
    db_review.rating = rating
    db_review.book_id = book_id
    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    """ Delete the review accounting to the review_id

    :param db: Session
    :param review_id: int
    :return: str
    """
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_review)
    db.commit()
    return "Review deleted successfully"
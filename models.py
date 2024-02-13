from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship


Base = declarative_base()

class Book(Base):
    """
        Book model is used for the db connection with books table
    """
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publication_year = Column(Integer)

    reviews = relationship("Review", back_populates="book")

class Review(Base):
    """
        Review model is used for the db connection with reviews table
    """
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    rating = Column(Integer)

    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="reviews")

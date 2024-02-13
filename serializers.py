from pydantic import BaseModel


class BookCreate(BaseModel):
    """
        This is the BookCreate for formatting the Book create request
    """
    title: str
    author: str
    publication_year: int

class BookResponse(BaseModel):
    """
        This is the BookResponse for formatting the Book response
    """
    id: int
    title: str
    author: str
    publication_year: int

class ReviewCreate(BaseModel):
    """
        This is the ReviewCreate for formatting the Review create request
    """
    text: str
    rating: int
    book_id: int

class ReviewResponse(BaseModel):
    """
        This is the ReviewResponse for formatting the Review response
    """
    id: int
    text: str
    rating: int
    book_id: int
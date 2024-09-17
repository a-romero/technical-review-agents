from pydantic import BaseModel

class ReviewComment(BaseModel):
    comment: str
    review: str
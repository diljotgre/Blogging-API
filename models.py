from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    title: str
    content: str
    category: str
    tags: list
    createdAt: datetime
    updatedAt: datetime
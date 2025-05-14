from typing import Optional
from pydantic import BaseModel

class BlogModel(BaseModel):
    title : str
    sub_title : str
    content : str
    author: str
    tags: str

class UpdateBlogModel(BaseModel):
    title : Optional[str] = None
    sub_title : Optional[str] = None
    content : Optional[str] = None
    author: Optional[str] = None
    tags: Optional[str] = None
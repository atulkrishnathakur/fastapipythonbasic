from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool

obj = Blog(title="My first class",is_active=True)
obj2 = Blog(title="My first class",description="This is good for the India",is_active=True)
obj3 = Blog(title="My first class",description=123,is_active=True)

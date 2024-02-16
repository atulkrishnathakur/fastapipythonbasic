from pydantic import BaseModel
from typing import List,Optional

class Comment(BaseModel):
    text: Optional[str] = None

class Blog(BaseModel):
    title: str
    comment: Optional[List[Comment]]
    is_active: bool


print(Blog(title="Hello World",comment=[{'text':'My Comment'},{'text':'Your comment'}],is_active=True))
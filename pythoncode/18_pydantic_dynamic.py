import time
from datetime import datetime
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str
    #created_at: datetime = datetime.now()
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool

print(Blog(title="My first blog",is_active=True))
time.sleep(10)
print(Blog(title="My second blog",is_active=True))


#Note: created_at field get value by default but if I used created_at: datetime = datetime.now() and object again print two time then output will be same
#Not2: If I used Field(default_factory=datetime.now) then pydantic store actual value in created_at field.

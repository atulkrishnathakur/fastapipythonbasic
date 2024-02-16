from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(...,min_length=5) # min_length is a hooks in pydantic
    is_active: bool

Blog(title='krishna',is_active=False)
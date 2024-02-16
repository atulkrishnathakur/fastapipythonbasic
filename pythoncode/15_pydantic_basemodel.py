from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    is_active:bool

obj = Blog(title="hello world",is_active = True) 
#obj = Blog(title="hello world",is_active = "Atul") # return error
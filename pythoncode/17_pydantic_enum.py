from pydantic import BaseModel
from enum import Enum

class Languages(str,Enum): # It will accept only one data type and Enum
    PYTHON = 'python'
    JAVA = 'java'
    GO = 'go'

class Blog(BaseModel):
    title: str
    #language: Languages # is accept Languages type
    language: Languages = Languages.JAVA # Languages.JAVA is default
    is_active: bool

#obj1 = Blog(title="First Blog",language='c',is_active=True) # It will give error
obj2 = Blog(title="First Blog",is_active=True) 
obj3 = Blog(title="Second Blog",language='go', is_active=True) 

print(obj3.language.value) # It will return value
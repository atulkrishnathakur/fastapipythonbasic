from pydantic import BaseModel, root_validator

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @root_validator()
    def veryfy_password_match(cls,values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("The two password did not match")
        return values


CreateUser(email="atul@yopmail.com",password='12345',confirm_password='1234')

# We have need to learn again
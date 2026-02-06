from pydantic import BaseModel

class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    user : str
    email : str
    password : str
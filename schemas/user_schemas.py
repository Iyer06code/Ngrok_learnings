from pydantic import BaseModel


class UserSchema(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str

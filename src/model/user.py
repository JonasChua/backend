# src/model/user.py

from pydantic import BaseModel, ConfigDict, Field

password_description = "Must be at least 8 characters long, contains at least 1 number, 1 uppercase letter, 1 lowercase letter and 1 special character"


class UserCreate(BaseModel):
    username: str = Field(examples=["user_name"])
    password: str = Field(examples=["P@ssw0rD!"], description=password_description)
    name: str = Field(examples=["name"])


class UserResponse(BaseModel):
    username: str
    name: str

    model_config = ConfigDict(from_attributes=True)

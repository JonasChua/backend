# src/model/user.py

from pydantic import BaseModel, ConfigDict, Field


class UserCreate(BaseModel):
    username: str = Field(examples=["user_name"])
    name: str = Field(examples=["name"])


class UserResponse(BaseModel):
    username: str
    name: str

    model_config = ConfigDict(from_attributes=True)

from typing import Optional, TypeVar, Dict
from pydantic import BaseModel, Field

from backend.src.app import get_password_hash

T = TypeVar('T')

""""
    General
"""


class Parameter(BaseModel):
    data: Dict[str, str] = None


class RequestSchema(BaseModel):
    parameter: Parameter = Field(...)


class ResponseSchema(BaseModel):
    code: str
    status: str
    message: str
    headers: Optional[T] = None
    result: Optional[T] = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class TokenVerify(BaseModel):
    token: str

"""
    Authentication
"""

class LoginSchema(BaseModel):
    email: str
    password: str


"""
    Users
"""

class RegisterSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    @property
    def get_password_hash(self):
        return get_password_hash(self.password)

from datetime import datetime
from typing import Optional, TypeVar, Dict
from pydantic import BaseModel, Field


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


class UpdateUserSchema(BaseModel):
    first_name: str
    last_name: str


"""
    Debts
"""

class DebtsSchema(BaseModel):
    user_id: int
    category_id: int
    title: str
    amount: float
    due_date: datetime
    status: str
    notes: Optional[str] = None
    is_deleted: bool



"""
    Category
"""

class CategorySchema(BaseModel):
    user_id: int
    name: str
    description: str
    color_rgb: str




"""
     Payment Historic
"""

class PaymentHistorySchema(BaseModel):
    user_id: int
    debt_id: int
    amount_paid: float
    payment_date: datetime
    payment_method: str
    notes: str
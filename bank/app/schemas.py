from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class AccountCreate(BaseModel):
    initial_deposit: Optional[float] = 0.0

class AccountOut(BaseModel):
    id: int
    agency: str
    number: int
    balance: float

    class Config:
        orm_mode = True

class TransactionType(str, Enum):
    deposit = "deposit"
    withdraw = "withdraw"

class TransactionCreate(BaseModel):
    type: TransactionType
    amount: float = Field(..., gt=0)
    description: Optional[str] = None

class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: TransactionType
    amount: float
    timestamp: datetime
    description: Optional[str]

    class Config:
        orm_mode = True

class StatementOut(BaseModel):
    account: AccountOut
    transactions: List[TransactionOut]

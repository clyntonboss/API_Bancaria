from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db import Base

class TransactionType(str, enum.Enum):
    deposit = "deposit"
    withdraw = "withdraw"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    accounts = relationship("Account", back_populates="owner")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    agency = Column(String(10), default="0001")
    number = Column(Integer, nullable=False, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    balance = Column(Float, default=0.0)

    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account", order_by="Transaction.timestamp")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    description = Column(String(255), nullable=True)

    account = relationship("Account", back_populates="transactions")

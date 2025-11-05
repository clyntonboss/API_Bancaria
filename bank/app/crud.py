from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app import models
from app.auth import get_password_hash, verify_password
from typing import Optional
from datetime import datetime

async def create_user(db: AsyncSession, username: str, password: str) -> models.User:
    hashed = get_password_hash(password)
    db_user = models.User(username=username, hashed_password=hashed)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def authenticate_user(db: AsyncSession, username: str, password: str) -> Optional[models.User]:
    q = await db.execute(select(models.User).where(models.User.username == username))
    user = q.scalars().first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

async def create_account(db: AsyncSession, owner: models.User, initial_deposit: float = 0.0) -> models.Account:
    q = await db.execute(select(func.count(models.Account.id)))
    total = q.scalar_one()
    number = total + 1
    account = models.Account(owner_id=owner.id, number=number, balance=0.0)
    db.add(account)
    await db.flush()
    if initial_deposit and initial_deposit > 0:
        account.balance += initial_deposit
        txn = models.Transaction(account=account, type=models.TransactionType.deposit, amount=initial_deposit, description="Initial deposit")
        db.add(txn)
    await db.commit()
    await db.refresh(account)
    return account

async def get_account_by_id(db: AsyncSession, account_id: int) -> Optional[models.Account]:
    q = await db.execute(select(models.Account).where(models.Account.id == account_id))
    return q.scalars().first()

async def list_accounts_for_user(db: AsyncSession, user: models.User):
    q = await db.execute(select(models.Account).where(models.Account.owner_id == user.id))
    return q.scalars().all()

async def create_transaction(db: AsyncSession, account: models.Account, txn_type: models.TransactionType, amount: float, description: str | None = None):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if txn_type == models.TransactionType.withdraw:
        if amount > account.balance:
            raise ValueError("Insufficient funds")
    if txn_type == models.TransactionType.deposit:
        account.balance += amount
    else:
        account.balance -= amount
    txn = models.Transaction(account=account, type=txn_type, amount=amount, description=description, timestamp=datetime.utcnow())
    db.add(txn)
    db.add(account)
    await db.commit()
    await db.refresh(txn)
    await db.refresh(account)
    return txn

async def get_statement(db: AsyncSession, account: models.Account):
    q = await db.execute(select(models.Transaction).where(models.Transaction.account_id == account.id).order_by(models.Transaction.timestamp))
    txns = q.scalars().all()
    return txns

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app import schemas, crud, models
from app.db import get_session
from app.auth import get_current_user

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=schemas.AccountOut)
async def create_account(account_in: schemas.AccountCreate, db: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_user)):
    account = await crud.create_account(db, user, initial_deposit=account_in.initial_deposit or 0.0)
    return account

@router.get("/", response_model=List[schemas.AccountOut])
async def list_my_accounts(db: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_user)):
    accounts = await crud.list_accounts_for_user(db, user)
    return accounts

@router.post("/{account_id}/transactions", response_model=schemas.TransactionOut)
async def create_transaction(account_id: int, txn_in: schemas.TransactionCreate, db: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_user)):
    account = await crud.get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized for this account")
    try:
        txn = await crud.create_transaction(db, account, models.TransactionType(txn_in.type.value), txn_in.amount, txn_in.description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return txn

@router.get("/{account_id}/statement", response_model=schemas.StatementOut)
async def get_statement(account_id: int, db: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_user)):
    account = await crud.get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized for this account")
    txns = await crud.get_statement(db, account)
    return {"account": account, "transactions": txns}

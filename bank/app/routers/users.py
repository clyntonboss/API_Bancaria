from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select as _select
from app import schemas, crud, models
from app.db import get_session
from app.auth import create_access_token

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=schemas.UserOut)
async def register_user(user_in: schemas.UserCreate, db: AsyncSession = Depends(get_session)):
    res = await db.execute(_select(models.User).where(models.User.username == user_in.username))
    exists = res.scalars().first()
    if exists:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = await crud.create_user(db, user_in.username, user_in.password)
    return user

@router.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

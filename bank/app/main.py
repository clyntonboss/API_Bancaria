from fastapi import FastAPI
from app.db import engine, Base
from app.routers.users import router as users_router
from app.routers.accounts import router as accounts_router

app = FastAPI(title="Bank API - FastAPI Async", version="1.0")

app.include_router(users_router)
app.include_router(accounts_router)

@app.on_event("startup")
async def on_startup():
    # create DB tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

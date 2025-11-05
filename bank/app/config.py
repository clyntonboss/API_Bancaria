import os
from dotenv import load_dotenv
load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "CHANGE_THIS_SECRET_TO_A_SECURE_RANDOM_STRING")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./bank.db")

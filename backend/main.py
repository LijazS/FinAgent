from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import os
from dotenv import load_dotenv

from pydantic import BaseModel
from typing import Optional, List

from database import get_db
import models
import schemas
from auth import get_password_hash, verify_password
from database import engine, Base
from auth import create_access_token

load_dotenv()

app = FastAPI() 
secret_key = os.getenv("SECRET_KEY")

origins = [
    "http://localhost:5173",  # Vite's default port
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Allow these origins
    allow_credentials=True,
    allow_methods=["*"],        # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],        # Allow all headers (Auth, etc.)
)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}



############################ USER REGISTRATION ###############################

@app.post("/signup", response_model=schemas.UserResponse)
async def signup(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    print(user)

    # Check if email already exists
    stmt = select(models.User).where(models.User.email == user.email)
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Hash password using your bcrypt function
    hashed_pw = get_password_hash(user.password)

    # Create user object
    new_user = models.User(
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    token = create_access_token(data={"sub": str(new_user.email)}, secret_key=secret_key)

    return {
        "id": str(new_user.id),
        "email": new_user.email,
        "token": token  # Placeholder for JWT or other token
    }


#############################  END USER REGISTRATION  ###############################

############################ USER LOGIN ###############################

@app.post("/login", response_model=schemas.LoginResponse)
async def login(user: schemas.UserLogin, db: AsyncSession = Depends(get_db)):
    stmt = select(models.User).where(models.User.email == user.email)
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()

    if not existing_user:
        raise HTTPException(status_code=400, detail="Email doesnt exist, Please sign up")
    
    if not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    token = create_access_token(data={"sub": str(existing_user.email)}, secret_key=secret_key)
    
    return {
        "id": str(existing_user.id),
        "email": existing_user.email,
        "token": token  # Placeholder for JWT or other token
    }

#############################  END USER LOGIN  ###############################




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
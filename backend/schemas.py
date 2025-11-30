from pydantic import BaseModel, EmailStr
from uuid import UUID

# --- USERS ---------
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID           # match the UUID from the DB
    email: EmailStr
    token: str | None = None

    class Config:
        orm_mode = True  # <-- must be orm_mode, not from_attributes

# --- LOGIN ---------
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    id: str           # UUID as string
    email: EmailStr
    # optionally add token if using JWT
    token: str | None = None

    class Config:
        orm_mode = True

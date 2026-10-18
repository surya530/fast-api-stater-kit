from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse, UserWithAddressCreate

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.post('/create')
def c_users():
    return { "data" : "user created." }

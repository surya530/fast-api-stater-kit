from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Address, User
from app.schemas import AddressCreate, AddressResponse

router = APIRouter(prefix="/addresses", tags=["Addresses"])
from pydantic import BaseModel, ConfigDict, EmailStr


class AddressCreate(BaseModel):
    country: str
    state: str


class AddressResponse(AddressCreate):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: AddressResponse | None = None

    model_config = ConfigDict(from_attributes=True)


class UserWithAddressCreate(UserCreate):
    address: AddressCreate
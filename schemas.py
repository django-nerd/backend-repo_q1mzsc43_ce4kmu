from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Lead capture and core app schemas for AgriForce Robotics

class Contact(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    message: Optional[str] = Field(None, description="Message or inquiry")
    country: Optional[str] = Field(None, description="Country")

class QuoteRequest(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    farm_size_acres: Optional[float] = Field(None, ge=0)
    crop_type: Optional[str] = None
    service: str = Field(..., description="Requested service")
    location: Optional[str] = None
    notes: Optional[str] = None

class Booking(BaseModel):
    name: str
    email: EmailStr
    phone: str
    preferred_date: Optional[str] = Field(None, description="Preferred visit date")
    farm_location: Optional[str] = None
    service: str
    farm_size_acres: Optional[float] = Field(None, ge=0)

class Subscription(BaseModel):
    email: EmailStr

# Keep previous example schemas if needed by other tools
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class ProductBase(BaseModel):
    name: str
    category: str
    price: float


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CustomerBase(BaseModel):
    name: str
    email: EmailStr


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    unit_price: Optional[float] = None


class OrderItemRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(BaseModel):
    customer_id: int
    order_date: Optional[datetime] = None
    status: Optional[str] = "created"
    items: List[OrderItemCreate]

    @field_validator("items")
    @classmethod
    def validate_items(cls, items):
        if not items:
            raise ValueError("Order must have at least one item.")
        return items


class OrderRead(BaseModel):
    id: int
    customer_id: int
    order_date: datetime
    status: str
    items: List[OrderItemRead]

    model_config = ConfigDict(from_attributes=True)


class SalesPoint(BaseModel):
    period_start: datetime
    revenue: float


class TopProduct(BaseModel):
    product_id: int
    product_name: str
    category: str
    revenue: float
    quantity: int


class CategorySummary(BaseModel):
    category: str
    revenue: float
    quantity: int


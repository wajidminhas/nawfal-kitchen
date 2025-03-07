from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int
    table_id: int
    status: str = "pending"  # pending, preparing, ready, delivered, canceled
    created_at: datetime = Field(default_factory=datetime.utcnow)
    items: List["OrderItem"] = Relationship(back_populates="order")


    
class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    dish_id: int
    quantity: int
    special_instructions: Optional[str] = None
    order: Order = Relationship(back_populates="items")
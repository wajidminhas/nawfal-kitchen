from sqlmodel import SQLModel, Field
from typing import Optional

class Dish(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str = "pending"  # pending, cooking, ready
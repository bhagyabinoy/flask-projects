from datetime import datetime
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    quantity: int
    created: datetime = datetime.utcnow()
    modified: datetime = datetime.utcnow()

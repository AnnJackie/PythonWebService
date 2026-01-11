from typing import Optional
from pydantic import BaseModel
from enum import Enum

class CustomerStatus(Enum):
    VIP = "VIP"
    REGULAR = "REGULAR"

class Customer(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    status: CustomerStatus
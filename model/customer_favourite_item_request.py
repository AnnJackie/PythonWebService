from typing import Optional

from pydantic import BaseModel


class CustomerFavouriteItemRequest(BaseModel):
    id: Optional[int] = None
    customer_id: int
    item_name: str

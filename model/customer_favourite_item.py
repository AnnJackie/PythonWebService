from typing import Optional

from pydantic import BaseModel


class CustomerFavouriteItem(BaseModel):
    id: Optional[int] = None
    customer_id: int
    item_id: int

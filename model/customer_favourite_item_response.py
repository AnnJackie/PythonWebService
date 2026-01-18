from typing import Optional

from pydantic import BaseModel

from api.internal_api.seller_service.model.item_response import ItemResponse


class CustomerFavouriteItemResponse(BaseModel):
    id: Optional[int] = None
    customer_id: int
    item_response: ItemResponse

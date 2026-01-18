from typing import Optional, List

from api.internal_api.seller_service import seller_service_api
from model.customer_favourite_item import CustomerFavouriteItem
from model.customer_favourite_item_request import CustomerFavouriteItemRequest
from model.customer_favourite_item_response import CustomerFavouriteItemResponse
from repository import customer_favourite_item_repository
from service import customer_service


async def get_by_id(favourite_item_id:int) -> Optional[CustomerFavouriteItemResponse]:
    customer_favourite_item = await customer_favourite_item_repository.get_by_id(favourite_item_id)
    if customer_favourite_item is not None:
        item = await seller_service_api.get_item_by_item_id(customer_favourite_item.item_id)
        if item is not None:
            return CustomerFavouriteItemResponse(
                id=customer_favourite_item.id,
                customer_id=customer_favourite_item.customer_id,
                item_response=item
            )
    return None

async def get_favourite_items_by_customer_id(customer_id: int) -> List[CustomerFavouriteItemResponse]:
    customer_favourite_items = await customer_favourite_item_repository.get_favourite_items_by_customer_id(customer_id)
    response_list = [
        CustomerFavouriteItemResponse(
            id=favourite_item.id,
            customer_id=favourite_item.customer_id,
            item_response=await seller_service_api.get_item_by_item_id(favourite_item.item_id)
        )
    for favourite_item in customer_favourite_items]
    return response_list

async def create_favourite_item(customer_favourite_item_request: CustomerFavouriteItemRequest) -> Optional[int]:
    customer = await customer_service.get_by_id(customer_favourite_item_request.customer_id)
    if customer is not None:
        item_details = await seller_service_api.get_lowest_price_item_by_name(customer_favourite_item_request.item_name)
        print(item_details)
        if item_details is not None:
            existing_favourite_item = await customer_favourite_item_repository.get_by_customer_id_and_item_id(customer.id, item_details.id)
            if existing_favourite_item is None:
                return await customer_favourite_item_repository.create_favourite_item(CustomerFavouriteItem(customer_id=customer.id, item_id=item_details.id))
    return None


async def update_favourite_item(favorite_item_id: int, favorite_item: CustomerFavouriteItem):
    await customer_favourite_item_repository.update_favourite_item(favorite_item_id, favorite_item)


async def delete_by_id(favorite_item_id: int):
    await customer_favourite_item_repository.delete_by_id(favorite_item_id)




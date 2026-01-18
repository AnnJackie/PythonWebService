from fastapi import APIRouter, HTTPException
from typing import List, Optional
from model.customer_favourite_item import CustomerFavouriteItem
from model.customer_favourite_item_request import CustomerFavouriteItemRequest
from model.customer_favourite_item_response import CustomerFavouriteItemResponse
from service import customer_favourite_item_service

router = APIRouter(
    prefix="/customer_favourite",
    tags=["customer_favourite"]
)


@router.get("/{favourite_item_id}", response_model=CustomerFavouriteItemResponse)
async def get_favourite_item(favourite_item_id: int) -> Optional[CustomerFavouriteItemResponse]:
    favourite_item = await customer_favourite_item_service.get_by_id(favourite_item_id)
    if not favourite_item:
        raise HTTPException(status_code=404, detail=f"Favourite item with id: {favourite_item_id} not found")
    return favourite_item


@router.get("/customer/{customer_id}", response_model=List[CustomerFavouriteItemResponse])
async def get_favourite_items_by_customer_id(customer_id: int) -> List[CustomerFavouriteItemResponse]:
    return await customer_favourite_item_service.get_favourite_items_by_customer_id(customer_id)


@router.post("/")
async def create_favourite_item(favourite_item: CustomerFavouriteItemRequest):
    return await customer_favourite_item_service.create_favourite_item(favourite_item)


@router.put("/{favourite_item_id}")
async def update_favourite_item(favourite_item_id: int, favourite_item: CustomerFavouriteItem):
    existing_favourite_item = await customer_favourite_item_service.get_by_id(favourite_item_id)
    if not existing_favourite_item:
        raise HTTPException(status_code=404,
                            detail=f"Can't update favourite item with id: {favourite_item_id}, item not found")
    await customer_favourite_item_service.update_favourite_item(favourite_item_id, favourite_item)
    return {"message": "Favourite item updated successfully"}


@router.delete("/{favourite_item_id}", response_model=dict)
async def delete_favourite_item(favourite_item_id: int):
    await customer_favourite_item_service.delete_by_id(favourite_item_id)
    return {"message": "Favourite item deleted successfully"}



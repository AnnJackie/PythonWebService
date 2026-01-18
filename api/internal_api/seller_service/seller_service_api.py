
import httpx

from config.config import Config
from api.internal_api.seller_service.model.item_response import ItemResponse

config = Config()

async def get_item_by_item_id(item_id):
    url = f"{config.SELLER_SERVICE_BASE_URL}/item/{item_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            item = ItemResponse(
                id=data.get('id'),
                item_name=data.get('item_name'),
                price=data.get('price')
            )
            return item

        except httpx.HTTPStatusError as exc:
            print(f"No item found with id: {item_id}")
            return None

async def get_lowest_price_item_by_name(item_name):
    url = f"{config.SELLER_SERVICE_BASE_URL}/item/search/"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params={"item_name": item_name})
            response.raise_for_status()
            data = response.json()
            item = ItemResponse(
                id=data.get('id'),
                item_name=data.get('item_name'),
                price = data.get('price')
            )
            return item
        except httpx.HTTPStatusError as exc:
            print(f"No item found with name: {item_name}\n{exc}")
            return None

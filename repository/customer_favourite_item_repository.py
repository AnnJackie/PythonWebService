from idlelib.editor import darwin
from typing import Optional

from model.customer_favourite_item import CustomerFavouriteItem
from repository.database import database

TABLE_NAME = 'customer_favourite_item'

async def get_by_id(favourite_item_id: int) -> Optional[CustomerFavouriteItem]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id = :favourite_item_id"
    result = await database.fetch_one(query, values={"favourite_item_id": favourite_item_id})
    if result:
        return CustomerFavouriteItem(**result)
    else:
        return None

async def get_favourite_items_by_customer_id(customer_id: int) -> list[CustomerFavouriteItem]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE customer_id = :customer_id"
    results = await database.fetch_all(query, values={"customer_id": customer_id})
    return [CustomerFavouriteItem(**result) for result in results]

async def get_by_customer_id_and_item_id(customer_id: int, item_id: int) -> Optional[CustomerFavouriteItem]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE customer_id = :customer_id AND item_id = :item_id"
    result = await database.fetch_one(query, values={"customer_id": customer_id, "item_id": item_id})
    if result:
        return CustomerFavouriteItem(**result)
    else:
        return None

async def create_favourite_item(favourite_item: CustomerFavouriteItem) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (customer_id, item_id)
        VALUES (:customer_id, :item_id)
    """
    values={"customer_id": favourite_item.customer_id, "item_id": favourite_item.item_id}
    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return last_record_id[0]

async def update_favourite_item(favourite_item_id: int, favourite_item: CustomerFavouriteItem):
    query = f"""
        UPDATE {TABLE_NAME}
            SET customer_id=:customer_id,
            item_id=:item_id
        WHERE id := favourite_item_id
    """
    values={"favourite_item_id": favourite_item_id,
            "customer_id": favourite_item.customer_id,
            "item_id": favourite_item.item_id}
    await database.execute(query, values)

async def delete_by_id(favourite_item_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:favourite_item_id"
    await database.execute(query, values={"favourite_item_id": favourite_item_id})
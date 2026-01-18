import json

from model.customer import Customer, CustomerStatus
from repository import cache_repository
from repository.database import database

customer_fields = ['first_name', 'last_name', 'email', 'status']

async def get_by_id(customer_id: int):
    if cache_repository.does_key_exists(str(customer_id)):
        string_customer = cache_repository.get_cache_entity(str(customer_id))
        customer_data = json.loads(string_customer)
        return Customer(**customer_data)
    else:
        query = "SELECT * FROM customer WHERE id=:customer_id"
        result = await database.fetch_one(query, values={"customer_id": customer_id})
        if result:
            customer = Customer(**result)
            cache_repository.create_cache_entity(str(customer_id), customer.json())
            return customer
        else:
            return None


async def get_all():
    query = "SELECT * FROM customer"
    return await database.fetch_all(query)

async def create_customer(customer: Customer):
    query = """
        INSERT INTO customer (first_name, last_name, email, status)
        VALUES (:first_name, :last_name, :email, :status)
    """
    values = {
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
        "status": customer.status.name,
    }

    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    cache_repository.create_cache_entity(str(customer.id), customer.json())
    return last_record_id[0]

async def update_customer(customer_id: int, customer: Customer):
    if cache_repository.does_key_exists(str(customer_id)):
        cache_repository.update_cache_entity(str(customer_id), customer.json())

    query = """
        UPDATE customer
        SET first_name=:first_name,
        last_name=:last_name,
        email=:email,
        status=:status
        WHERE id = :customer_id
    """
    values = {
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
        "status": customer.status.name,
        "customer_id": customer_id,
    }
    await database.execute(query, values)


async def delete_by_id(customer_id: int):
    cache_repository.remove_cache_entity(str(customer_id))

    query = "DELETE FROM customer WHERE id=:customer_id"
    return await database.execute(query, values={"customer_id": customer_id})


async def get_by_status(customer_status: CustomerStatus):
    query = "SELECT * FROM customer WHERE status=:customer_status"
    return await database.fetch_all(query, values={"customer_status": customer_status.name})
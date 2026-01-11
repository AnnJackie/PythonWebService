from model.customer import Customer, CustomerStatus
from repository.database import database

customer_fields = ['first_name', 'last_name', 'email', 'status']

async def get_by_id(customer_id: int):
    query = "SELECT * FROM customer WHERE id=:customer_id"
    return await database.fetch_one(query, values={"customer_id": customer_id})

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

    await database.execute(query, values)

async def update_customer(customer_id: int, customer: Customer):
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
    query = "DELETE FROM customer WHERE id=:customer_id"
    return await database.execute(query, values={"customer_id": customer_id})


async def get_by_status(customer_status: CustomerStatus):
    query = "SELECT * FROM customer WHERE status=:customer_status"
    return await database.fetch_all(query, values={"customer_status": customer_status.name})
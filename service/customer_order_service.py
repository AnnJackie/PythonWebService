from fastapi import HTTPException
from starlette import status

from model.customer import Customer
from model.customer_order import CustomerOrder
from model.customer_order_request import CustomerOrderRequest
from model.customer_order_response import CustomerOrderResponse
from repository import customer_order_repository
from service import customer_service


async def get_by_id(customer_order_id):
    return await customer_order_repository.get_by_id(customer_order_id)


async def create_customer_order(customer_order_request: CustomerOrderRequest) -> CustomerOrderResponse:
    selected_customer = customer_order_request.customer

    if selected_customer.id is None:
        created_customer_id = await customer_service.create_customer(selected_customer)
        record = await customer_service.get_by_id(created_customer_id)
        selected_customer = Customer(**dict(record))
        customer_order_request.customer_order.customer_id = created_customer_id
    else:
        existing_customer = await customer_service.get_by_id(selected_customer.id)
        if existing_customer is None or existing_customer.id is None:
            raise Exception(f"Can't find customer with id {existing_customer.id}")

    customer_order_request.customer = selected_customer
    customer_order = customer_order_request.customer_order

    await customer_order_repository.create_customer_order(customer_order)
    raw_orders = await customer_order_repository.get_by_customer_id(selected_customer.id)
    customer_orders = [CustomerOrder(**dict(record)) for record in raw_orders]

    return CustomerOrderResponse(customer=selected_customer, customer_orders=customer_orders)


async def update_customer_order(customer_order_id, customer_order_request):
    existing_order_record = await customer_order_repository.get_by_id(customer_order_id)
    if not existing_order_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"CustomerOrder with id {customer_order_id} does not exist."
        )
    existing_order = CustomerOrder(**dict(existing_order_record))
    updated_order_data = customer_order_request.customer_order
    existing_order.item_name = updated_order_data.item_name
    existing_order.price = updated_order_data.price
    existing_order.customer_id = existing_order.customer_id

    await customer_order_repository.update_customer_order(customer_order_id, existing_order)

    customer_id = existing_order.customer_id
    customer_record = await customer_service.get_by_id(customer_id)
    if not customer_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with id {customer_id} not found."
        )
    customer = Customer(**dict(customer_record))  # <-- fix here
    raw_orders = await customer_order_repository.get_by_customer_id(customer_id)
    customer_orders = [CustomerOrder(**dict(r)) for r in raw_orders]

    return CustomerOrderResponse(customer=customer, customer_orders=customer_orders)

async def delete_by_id(customer_order_id):
    return await customer_order_repository.delete_by_id(customer_order_id)
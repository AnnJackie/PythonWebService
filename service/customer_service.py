from typing import List, Optional

from fastapi import HTTPException
from starlette import status

from model.customer import Customer, CustomerStatus
from repository import customer_repository

MAX_VIP_CUSTOMERS_ALLOWED = 10

async def get_by_id(customer_id: int) -> Optional[Customer]:
    return await customer_repository.get_by_id(customer_id)


async def get_all() -> List[Customer]:
    return await customer_repository.get_all()


async def create_customer(customer: Customer) -> int:
    if customer.status == CustomerStatus.VIP:
        vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
        if len(vip_customers) < MAX_VIP_CUSTOMERS_ALLOWED:
            return await customer_repository.create_customer(customer)
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"No more than {MAX_VIP_CUSTOMERS_ALLOWED} VIP customers are allowed"
            )
    else:
        return await customer_repository.create_customer(customer)


async def update_customer(customer_id: int, customer: Customer) -> bool:
    existing_customer = await customer_repository.get_by_id(customer_id)
    if not existing_customer:
        return False

    if customer.status == CustomerStatus.VIP:
        if existing_customer.status != CustomerStatus.VIP:
            vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
            if len(vip_customers) < MAX_VIP_CUSTOMERS_ALLOWED:
                await customer_repository.update_customer(customer_id, customer)
                return True
            else:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"No more than {MAX_VIP_CUSTOMERS_ALLOWED} VIP customers are allowed"
                )
        else:
            await customer_repository.update_customer(customer_id, customer)
            return True
    else:
        await customer_repository.update_customer(customer_id, customer)
        return True


async def delete_customer(customer_id: int) -> bool:
    existing_customer = await customer_repository.get_by_id(customer_id)
    if not existing_customer:
        return False

    await customer_repository.delete_by_id(customer_id)
    return True

from typing import List

from fastapi import APIRouter, HTTPException, status

from model.customer import Customer
from service import customer_service

router = APIRouter(
    prefix="/customer",
    tags=["customer"]
)


@router.get("/{customer_id}", response_model=Customer)
async def get_customer_by_id(customer_id: int):
    customer = await customer_service.get_by_id(customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with id {customer_id} not found"
        )
    return customer


@router.get("/", response_model=List[Customer])
async def get_all_customers():
    return await customer_service.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    await customer_service.create_customer(customer)


@router.put("/{customer_id}")
async def update_customer(customer_id: int, customer: Customer):
    updated = await customer_service.update_customer(customer_id, customer)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with id {customer_id} not found"
        )


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: int):
    deleted = await customer_service.delete_customer(customer_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with id {customer_id} not found"
        )
from fastapi import APIRouter, HTTPException, Query, Header
from model.order import Order
from typing import List, Optional

router = APIRouter(
    prefix="/order",
    tags=["order"]
)

orders = {}

@router.get("/{order_id}", response_model=Order)
async def get_order(order_id: int, authorization: Optional[str] = Header(None)):
    if authorization:
        order = orders.get(order_id)
        if not order:
            raise HTTPException(status_code=404, detail=f"Order {order_id} was not found")
        return order
    else:
        raise HTTPException(status_code=401, detail="Unauthorized user")



@router.post("/", response_model=Order)
async def create_order(order: Order):
    if order.order_id in orders:
        raise HTTPException(status_code=400, detail=f"Order {order.order_id} already exists")
    orders[order.order_id] = order
    return order

@router.put("/{order_id}", response_model=Order)
async def update_order(order_id: int, updated_order: Order, api_key: str):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail=f"Order {order_id} was not found")
    orders[order_id] = updated_order
    return updated_order

@router.delete("/{order_id}", response_model=Order)
async def delete_order(order_id: int):
    order = orders.pop(order_id, None)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order {order_id} was not found")
    return order

@router.get("/", response_model=List[Order])
async def get_orders_by_customer(customer_name: Optional[str] = Query(None)) -> List[str]:
    orders_result = []
    for order in orders.values():
        if order.customer_name == customer_name:
            orders_result.append(order)
    return orders_result

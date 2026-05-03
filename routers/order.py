from models import Order
from routers.crud_factory import build_crud_router
from schemas import OrderBase, OrderOut

router = build_crud_router(
    model=Order,
    create_schema=OrderBase,
    response_schema=OrderOut,
    prefix="/orders",
    tag="Order",
)

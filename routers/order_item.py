from models import OrderItem
from routers.crud_factory import build_crud_router
from schemas import OrderItemBase, OrderItemOut

router = build_crud_router(
    model=OrderItem,
    create_schema=OrderItemBase,
    response_schema=OrderItemOut,
    prefix="/order-items",
    tag="OrderItem",
)

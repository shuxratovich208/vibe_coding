from models import CartItem
from routers.crud_factory import build_crud_router
from schemas import CartItemBase, CartItemOut

router = build_crud_router(
    model=CartItem,
    create_schema=CartItemBase,
    response_schema=CartItemOut,
    prefix="/cart-items",
    tag="CartItem",
)

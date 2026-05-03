from models import Discount
from routers.crud_factory import build_crud_router
from schemas import DiscountBase, DiscountOut

router = build_crud_router(
    model=Discount,
    create_schema=DiscountBase,
    response_schema=DiscountOut,
    prefix="/discounts",
    tag="Discount",
)

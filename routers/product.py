from models import Product
from routers.crud_factory import build_crud_router
from schemas import ProductBase, ProductOut

router = build_crud_router(
    model=Product,
    create_schema=ProductBase,
    response_schema=ProductOut,
    prefix="/products",
    tag="Product",
)

from models import Brand
from routers.crud_factory import build_crud_router
from schemas import BrandBase, BrandOut

router = build_crud_router(
    model=Brand,
    create_schema=BrandBase,
    response_schema=BrandOut,
    prefix="/brands",
    tag="Brand",
)

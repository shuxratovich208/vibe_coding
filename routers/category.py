from models import Category
from routers.crud_factory import build_crud_router
from schemas import CategoryBase, CategoryOut

router = build_crud_router(
    model=Category,
    create_schema=CategoryBase,
    response_schema=CategoryOut,
    prefix="/categories",
    tag="Category",
)

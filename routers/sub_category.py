from models import SubCategory
from routers.crud_factory import build_crud_router
from schemas import SubCategoryBase, SubCategoryOut

router = build_crud_router(
    model=SubCategory,
    create_schema=SubCategoryBase,
    response_schema=SubCategoryOut,
    prefix="/sub-categories",
    tag="SubCategory",
)

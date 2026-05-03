from models import VariantOption
from routers.crud_factory import build_crud_router
from schemas import VariantOptionBase, VariantOptionOut

router = build_crud_router(
    model=VariantOption,
    create_schema=VariantOptionBase,
    response_schema=VariantOptionOut,
    prefix="/variant-options",
    tag="VariantOption",
)

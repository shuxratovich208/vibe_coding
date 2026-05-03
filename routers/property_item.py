from models import Property
from routers.crud_factory import build_crud_router
from schemas import PropertyBase, PropertyOut

router = build_crud_router(
    model=Property,
    create_schema=PropertyBase,
    response_schema=PropertyOut,
    prefix="/properties",
    tag="Property",
)

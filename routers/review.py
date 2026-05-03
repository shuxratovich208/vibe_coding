from models import Review
from routers.crud_factory import build_crud_router
from schemas import ReviewBase, ReviewOut

router = build_crud_router(
    model=Review,
    create_schema=ReviewBase,
    response_schema=ReviewOut,
    prefix="/reviews",
    tag="Review",
)

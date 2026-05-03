from models import Image
from routers.crud_factory import build_crud_router
from schemas import ImageBase, ImageOut

router = build_crud_router(
    model=Image,
    create_schema=ImageBase,
    response_schema=ImageOut,
    prefix="/images",
    tag="Image",
)

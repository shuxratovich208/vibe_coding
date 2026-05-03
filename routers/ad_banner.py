from models import AdBanner
from routers.crud_factory import build_crud_router
from schemas import AdBannerBase, AdBannerOut

router = build_crud_router(
    model=AdBanner,
    create_schema=AdBannerBase,
    response_schema=AdBannerOut,
    prefix="/ad-banners",
    tag="AdBanner",
)

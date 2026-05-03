from models import Favorite
from routers.crud_factory import build_crud_router
from schemas import FavoriteBase, FavoriteOut

router = build_crud_router(
    model=Favorite,
    create_schema=FavoriteBase,
    response_schema=FavoriteOut,
    prefix="/favorites",
    tag="Favorite",
)

from models import User
from routers.crud_factory import build_crud_router
from schemas import UserBase, UserOut

router = build_crud_router(
    model=User,
    create_schema=UserBase,
    response_schema=UserOut,
    prefix="/users",
    tag="User",
)

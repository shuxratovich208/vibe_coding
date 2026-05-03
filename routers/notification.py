from models import Notification
from routers.crud_factory import build_crud_router
from schemas import NotificationBase, NotificationOut

router = build_crud_router(
    model=Notification,
    create_schema=NotificationBase,
    response_schema=NotificationOut,
    prefix="/notifications",
    tag="Notification",
)

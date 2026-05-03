from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from database.base import Base
from database.connection import engine
from routers import (
    ad_banner,
    brand,
    cart_item,
    category,
    discount,
    favorite,
    image,
    notification,
    order,
    order_item,
    product,
    property_item,
    review,
    sub_category,
    user,
    variant_option,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce API", version="1.0.0", docs_url="/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category.router)
app.include_router(sub_category.router)
app.include_router(brand.router)
app.include_router(product.router)
app.include_router(image.router)
app.include_router(property_item.router)
app.include_router(variant_option.router)
app.include_router(review.router)
app.include_router(favorite.router)
app.include_router(user.router)
app.include_router(cart_item.router)
app.include_router(order.router)
app.include_router(order_item.router)
app.include_router(ad_banner.router)
app.include_router(notification.router)
app.include_router(discount.router)


@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()
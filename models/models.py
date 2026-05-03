from sqlalchemy import Boolean, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    image: Mapped[str | None] = mapped_column(String(255), nullable=True)


class SubCategory(Base):
    __tablename__ = "sub_categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    image: Mapped[str | None] = mapped_column(String(255), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))


class Brand(Base):
    __tablename__ = "brands"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    logo: Mapped[str | None] = mapped_column(String(255), nullable=True)


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    details: Mapped[str | None] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(Float, default=0)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))
    sub_category_id: Mapped[int] = mapped_column(ForeignKey("sub_categories.id"))


class Image(Base):
    __tablename__ = "images"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    image: Mapped[str] = mapped_column(String(255))
    main: Mapped[bool] = mapped_column(Boolean, default=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))


class Property(Base):
    __tablename__ = "properties"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    value: Mapped[str] = mapped_column(String(120))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))


class VariantOption(Base):
    __tablename__ = "variant_options"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    image: Mapped[str | None] = mapped_column(String(255), nullable=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))


class Review(Base):
    __tablename__ = "reviews"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text: Mapped[str | None] = mapped_column(Text, nullable=True)
    rate: Mapped[int] = mapped_column(Integer, default=5)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))


class Favorite(Base):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    email: Mapped[str | None] = mapped_column(String(160), nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(40), nullable=True)


class CartItem(Base):
    __tablename__ = "cart_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    discount_id: Mapped[int | None] = mapped_column(ForeignKey("discounts.id"), nullable=True)
    amount: Mapped[int] = mapped_column(Integer, default=1)


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    phone_number: Mapped[str] = mapped_column(String(40))
    address: Mapped[str] = mapped_column(String(255))
    total_price: Mapped[float] = mapped_column(Float, default=0)
    status: Mapped[str] = mapped_column(String(40), default="new")
    delivery_type: Mapped[str] = mapped_column(String(40), default="standard")
    payment_type: Mapped[str] = mapped_column(String(40), default="cash")


class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    amount: Mapped[int] = mapped_column(Integer, default=1)
    discount_id: Mapped[int | None] = mapped_column(ForeignKey("discounts.id"), nullable=True)


class AdBanner(Base):
    __tablename__ = "ad_banners"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(120))
    cover: Mapped[str | None] = mapped_column(String(255), nullable=True)
    details: Mapped[str | None] = mapped_column(Text, nullable=True)
    url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)


class Notification(Base):
    __tablename__ = "notifications"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(120))
    details: Mapped[str | None] = mapped_column(Text, nullable=True)
    cover: Mapped[str | None] = mapped_column(String(255), nullable=True)
    seen: Mapped[bool] = mapped_column(Boolean, default=False)
    url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class Discount(Base):
    __tablename__ = "discounts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sale: Mapped[str | None] = mapped_column(String(120), nullable=True)
    percentage: Mapped[float] = mapped_column(Float, default=0)
    start_date: Mapped[str | None] = mapped_column(String(40), nullable=True)
    end_date: Mapped[str | None] = mapped_column(String(40), nullable=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

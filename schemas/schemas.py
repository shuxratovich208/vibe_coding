from pydantic import BaseModel


class ORMBase(BaseModel):
    class Config:
        from_attributes = True


class CategoryBase(ORMBase):
    name: str
    image: str | None = None


class CategoryOut(CategoryBase):
    id: int


class SubCategoryBase(ORMBase):
    name: str
    image: str | None = None
    category_id: int


class SubCategoryOut(SubCategoryBase):
    id: int


class BrandBase(ORMBase):
    name: str
    logo: str | None = None


class BrandOut(BrandBase):
    id: int


class ProductBase(ORMBase):
    name: str
    details: str | None = None
    price: float = 0
    brand_id: int
    sub_category_id: int


class ProductOut(ProductBase):
    id: int


class ImageBase(ORMBase):
    image: str
    main: bool = False
    product_id: int


class ImageOut(ImageBase):
    id: int


class PropertyBase(ORMBase):
    name: str
    value: str
    product_id: int


class PropertyOut(PropertyBase):
    id: int


class VariantOptionBase(ORMBase):
    name: str
    image: str | None = None
    product_id: int


class VariantOptionOut(VariantOptionBase):
    id: int


class ReviewBase(ORMBase):
    text: str | None = None
    rate: int = 5
    user_id: int
    product_id: int


class ReviewOut(ReviewBase):
    id: int


class FavoriteBase(ORMBase):
    user_id: int
    product_id: int


class FavoriteOut(FavoriteBase):
    id: int


class UserBase(ORMBase):
    username: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone_number: str | None = None


class UserOut(UserBase):
    id: int


class CartItemBase(ORMBase):
    user_id: int
    product_id: int
    discount_id: int | None = None
    amount: int = 1


class CartItemOut(CartItemBase):
    id: int


class OrderBase(ORMBase):
    user_id: int
    phone_number: str
    address: str
    total_price: float = 0
    status: str = "new"
    delivery_type: str = "standard"
    payment_type: str = "cash"


class OrderOut(OrderBase):
    id: int


class OrderItemBase(ORMBase):
    order_id: int
    product_id: int
    amount: int = 1
    discount_id: int | None = None


class OrderItemOut(OrderItemBase):
    id: int


class AdBannerBase(ORMBase):
    title: str
    cover: str | None = None
    details: str | None = None
    url: str | None = None
    active: bool = True


class AdBannerOut(AdBannerBase):
    id: int


class NotificationBase(ORMBase):
    title: str
    details: str | None = None
    cover: str | None = None
    seen: bool = False
    url: str | None = None
    user_id: int


class NotificationOut(NotificationBase):
    id: int


class DiscountBase(ORMBase):
    sale: str | None = None
    percentage: float = 0
    start_date: str | None = None
    end_date: str | None = None
    product_id: int


class DiscountOut(DiscountBase):
    id: int

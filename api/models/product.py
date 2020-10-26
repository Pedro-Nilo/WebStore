from api.models import db
from api.models.base import BaseModel
from sqlalchemy.orm import validates


class Product(db.Model, BaseModel):
    __tablename__ = "product"

    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    price = db.Column(db.DECIMAL(5, 2), default=0.01, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)

    item_on_orders = db.relationship("OrderItem", backref="order_item",
                                     lazy="dynamic")

    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise AssertionError("No product name provided")

        if Product.query.filter(Product.name == name).first():
            raise AssertionError("Product name is already in use")

        return name

    @validates("price")
    def validate_price(self, key, price):
        if not price:
            raise AssertionError("No price provided")

        if price <= 0.00:
            raise AssertionError(
                "Price must be a positive non-zero decimal")

        return price

    @validates("stock")
    def validate_stock(self, key, stock):
        if not stock:
            raise AssertionError("No stock provided")

        if stock < 0:
            raise AssertionError(
                "Stock must be a positive non-zero integer")

        return stock

    def __repr__(self):
        return "<Product %s>" % self.name

    def to_dict(self):
        return dict(id=self.id, name=self.name, price=str(self.price),
                    stock=self.stock)

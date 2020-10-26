from api.models import db
from api.models.base import BaseModel
from sqlalchemy.orm import validates


class OrderItem(db.Model, BaseModel):
    __tablename__ = "order_item"

    request_quantity = db.Column(db.Integer, default=0, nullable=False)
    item_price = db.Column(db.DECIMAL(5, 2), default=0.01, nullable=False)
    order_id = db.Column(db.ForeignKey("order.id"))
    product_id = db.Column(db.ForeignKey("product.id"))

    @validates("item_price")
    def validate_item_price(self, key, item_price):
        if not item_price:
            raise AssertionError("No price provided")

        if item_price <= 0.00:
            raise AssertionError(
                "Price must be a positive non-zero decimal")

        return item_price

    @validates("request_quantity")
    def validate_quantity(self, key, request_quantity):
        if not request_quantity:
            raise AssertionError("No quantity provided")

        if request_quantity < 0:
            raise AssertionError(
                "Quantity must be a positive non-zero integer")

        return request_quantity

    def __repr__(self):
        return "<Order Item %s>" % self.id

    def to_dict(self):
        return dict(id=self.id, product_id=self.product_id,
                    order_id=self.order_id, item_price=self.item_price,
                    quantity=self.request_quantity)

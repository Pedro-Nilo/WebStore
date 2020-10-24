from api.models import db
from api.models.base import BaseModel


class Product(db.Model, BaseModel):
    __tablename__ = "product"

    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    price = db.Column(db.DECIMAL(5, 2), default=0.00, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)

    item_on_orders = db.relationship("OrderItem", backref="order_item",
                                     lazy="dynamic")

    def __repr__(self):
        return "<Product %s>" % self.name

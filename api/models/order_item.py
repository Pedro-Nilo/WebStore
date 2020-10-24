from api.models import db
from api.models.base import BaseModel


class OrderItem(db.Model, BaseModel):
    __tablename__ = "order_item"

    request_quantity = db.Column(db.Integer, default=0, nullable=False)
    item_price = db.Column(db.DECIMAL(5, 2), default=0.00, nullable=False)
    order_id = db.Column(db.ForeignKey("order.id"))
    product_id = db.Column(db.ForeignKey("product.id"))

    def __repr__(self):
        return "<Order Item %s>" % self.id

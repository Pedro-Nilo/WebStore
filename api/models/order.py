from api.models import db
from api.models.base import BaseModel
from datetime import datetime
from sqlalchemy.orm import validates


class Order(db.Model, BaseModel):
    __tablename__ = "order"

    request_date = db.Column(db.DateTime, index=True, default=datetime.now,
                             nullable=False)
    price = db.Column(db.DECIMAL(5, 2), default=0.00, nullable=False)
    status = db.Column(db.BOOLEAN, nullable=False, default=True)
    reason = db.Column(db.String(255), nullable=True)
    client_id = db.Column(db.ForeignKey("user.id"))

    order_items = db.relationship("OrderItem", backref="order", lazy="dynamic")

    @validates("price")
    def validate_price(self, key, price):
        if not price:
            raise AssertionError("No price provided")

        if price < 0.00:
            raise AssertionError(
                "Price must be a positive decimal")

        return price

    def __repr__(self):
        return "<Order %s>" % self.id

    def to_dict(self):
        order_items_list = [
            order_item.to_dict() for order_item in self.order_items]

        if self.status:
            status = "Succeed"
        else:
            status = "Canceled"

        return dict(id=self.id, client_id=self.client_id,
                    request_date=self.request_date, total=str(self.price),
                    status=status, reason=self.reason,
                    order_items=order_items_list)

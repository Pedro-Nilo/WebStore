from api.models import db
from api.models.base import BaseModel
from datetime import datetime


class Order(db.Model, BaseModel):
    __tablename__ = "order"

    request_date = db.Column(db.DateTime, index=True, default=datetime.utcnow,
                             nullable=False)
    price = db.Column(db.DECIMAL(5, 2), default=0.00, nullable=False)
    status = db.Column(db.BOOLEAN, nullable=False)
    client_id = db.Column(db.ForeignKey("user.id"))

    order_items = db.relationship("OrderItem", backref="order", lazy="dynamic")

    def __repr__(self):
        return "<Order %s>" % self.id

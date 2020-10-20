from api.models import db
from api.models.base import BaseModel


class Product(db.Model, BaseModel):
    __tablename__ = "product"

    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.DECIMAL(5, 2), default=0.00)
    quantity = db.Column(db.Integer, default=0)

    def __repr__(self):
        return "<Product %s>" % self.name

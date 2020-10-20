from api.models import db
from api.models.base import BaseModel


class Customer(db.Model, BaseModel):
    __tablename__ = "customer"

    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    token = db.Column(db.String(128))

    def __repr__(self):
        return "<Customer %s>" % self.username

from api.models import db
from api.models.base import BaseModel


class User(db.Model, BaseModel):
    __tablename__ = "user"

    username = db.Column(db.String(64), index=True, unique=True,
                         nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    is_manager = db.Column(db.BOOLEAN, default=False, nullable=False)
    token = db.Column(db.String(128), nullable=False)

    orders = db.relationship("Order", backref="client", lazy="dynamic")

    def __repr__(self):
        return "<User %s>" % self.username

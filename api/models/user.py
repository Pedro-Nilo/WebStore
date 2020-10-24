import base64
import os
import re

from api.models import db
from api.models.base import BaseModel
from datetime import datetime, timedelta
from flask_login import UserMixin
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model, BaseModel):
    __tablename__ = "user"

    username = db.Column(db.String(64), index=True, unique=True,
                         nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_manager = db.Column(db.BOOLEAN, default=False, nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    orders = db.relationship("Order", backref="client", lazy="dynamic")

    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise AssertionError("No username provided")

        if User.query.filter(User.username == username).first():
            raise AssertionError("Username is already in use")

        if len(username) < 5 or len(username) > 20:
            raise AssertionError(
                "Username must be between 5 and 20 characters")

        return username

    @validates("email")
    def validate_email(self, key, email):
        if not email:
            raise AssertionError("No email provided")

        if not re.match("[^@]+@[^@]+\\.[^@]+", email):
            raise AssertionError("Provided email is not an email address")

        return email

    def __repr__(self):
        return "<User %s>" % self.username

    def set_password(self, password):
        if not password:
            raise AssertionError("Password not provided")

        if not re.match("\\d.*[A-Z]|[A-Z].*\\d", password):
            raise AssertionError(
                "Password must contain 1 capital letter and 1 number")

        if len(password) < 8 or len(password) > 50:
            raise AssertionError(
                "Password must be between 8 and 50 characters")

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return dict(id=self.id, username=self.username, email=self.email)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()

        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token

        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.token_expiration = now + timedelta(seconds=expires_in)

        db.session.add(self)

        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()

        if user is None or user.token_expiration < datetime.utcnow():
            return None

        return user

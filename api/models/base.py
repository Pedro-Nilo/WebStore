from api.models import db


class BaseModel():
    id = db.Column(db.Integer, primary_key=True)

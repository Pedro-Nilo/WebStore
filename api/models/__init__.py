from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


from api.models import user, product, order, order_item

from api import create_app
from api.models import db
from api.models.order import Order
from api.models.order_item import OrderItem
from api.models.product import Product
from api.models.user import User


webstore_api = create_app()


@webstore_api.shell_context_processor
def make_shell_context():
    return dict(db=db, Order=Order, OrderItem=OrderItem, Product=Product,
                User=User)

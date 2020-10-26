from api.models import db
from api.models.order import Order
from api.models.order_item import OrderItem
from api.models.product import Product
from decimal import Decimal


class OrderService:
    def add(self, client_id, request):

        data = request.get_json()

        if "products" not in data:
            return dict(message="No products list provided",
                        status_code=400)

        if not isinstance(data["products"], list):
            return dict(message="Products is not a list",
                        status_code=400)

        order = Order(client_id=client_id)

        db.session.add(order)
        db.session.commit()

        status = 201

        try:
            for item in data["products"]:
                if not isinstance(item, dict):
                    order.reason = "Item %s is malformed" % item
                    status = 400
                    break

                if "product_name" not in item:
                    order.reason = "Item %s no provide a product" % item
                    status = 400
                    break

                if "quantity" not in item:
                    order.reason = "Item %s no provide a quantity" % item
                    status = 400
                    break

                quantity = int(item["quantity"])

                if quantity < 0:
                    order.reason = \
                        "Item %s no provide a invalid quantity" % item
                    status = 400
                    break

                product = Product.query.filter_by(name=item["product_name"])\
                                 .first()

                if not product:
                    order.reason = \
                        "Item %s provide a nonexistent product" % item
                    status = 400
                    break

                if product.stock < quantity:
                    order.reason = \
                        "insufficient product %s quantity" % product.name
                    status = 400
                    break

                product.stock -= quantity

                order_item = OrderItem(order_id=order.id,
                                       product_id=product.id,
                                       request_quantity=quantity,
                                       item_price=Decimal(
                                           product.price * quantity))

                db.session.add(order_item)
                order.price = Decimal(order.price + order_item.item_price)

            if order.reason:
                order.status = False
        except Exception as exception_message:
            order.reason = "%s" % exception_message
            order.status = False
        finally:
            db.session.commit()

        order = Order.query.get(order.id).to_dict()

        return dict(message=order,
                    status_code=status)

    def get(self):
        orders = Order.query.all()

        orders_list = [order.to_dict() for order in orders]

        return dict(message=orders_list, status_code=200)

    def get_by_id(self, id, user_id=None):
        if user_id:
            order = Order.query.filter(Order.id == id,
                                       Order.client_id == user_id)\
                         .first()
        else:
            order = Order.query.get(id).to_dict()

        if order:
            return dict(message=order, status_code=200)
        else:
            return dict(message="Order with ID %s not found" % id,
                        status_code=404)

    def get_by_client_id(self, client_id):
        orders = Order.query.filter_by(client_id=client_id)

        orders_list = [order.to_dict() for order in orders]

        return dict(message=orders_list, status_code=200)

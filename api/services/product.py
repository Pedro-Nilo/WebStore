from api.models import db
from api.models.product import Product
from decimal import Decimal


class ProductService:
    def add(self, request):
        data = request.get_json()

        if "name" not in data:
            return dict(message="No name provided",
                        status_code=400)

        if "price" not in data:
            return dict(message="No price provided",
                        status_code=400)

        if "stock" not in data:
            return dict(message="No stock provided",
                        status_code=400)

        try:
            new_product = Product(name=data["name"],
                                  price=Decimal(
                                      data["price"].replace(",", ".")),
                                  stock=int(data["stock"]))

            db.session.add(new_product)

            db.session.commit()

            return dict(message=new_product.to_dict(),
                        status_code=201)
        except AssertionError as exception_message:
            return dict(message="%s" % exception_message,
                        status_code=400)

    def get(self):
        products = Product.query.all()

        products_list = [product.to_dict() for product in products]

        return dict(message=products_list, status_code=200)

    def get_by_name(self, name):
        product = Product.query.filter_by(name=name).first().to_dict()

        if product:
            return dict(message=product, status_code=200)
        else:
            return dict(message="Product with name %s not found" % name,
                        status_code=404)

    def update(self, id, request):
        target_product = Product.query.get(id)

        if not target_product:
            return dict(message="Product with ID %s not found" % id,
                        status_code=404)

        data = request.get_json()

        try:
            if "price" in data:
                target_product.price = Decimal(data["price"].replace(",", "."))

            if "stock" in data:
                target_product.stock = int(data["stock"])

            db.session.commit()

            return dict(message=target_product.to_dict(), status_code=200)
        except AssertionError as exception_message:
            return dict(message="%s" % exception_message,
                        status_code=400)

    def delete(self, id):
        target_product = Product.query.get(id).to_dict()

        if not target_product:
            return dict(message="Product with ID %s not found" % id,
                        status_code=404)
        else:
            Product.query.filter_by(id=id).delete()
            db.session.commit()

            return dict(message=target_product, status_code=200)

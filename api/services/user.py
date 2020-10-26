from api.models import db
from api.models.user import User


class UserService:
    def add_super(self, username, email, password):
        if not username:
            return dict(message="No username provided",
                        status_code=400)

        if not password:
            return dict(message="No password provided",
                        status_code=400)

        if not email:
            return dict(message="No email provided",
                        status_code=400)

        try:
            new_user = User(username=username,
                            email=email,
                            is_manager=True)

            new_user.set_password(password)

            db.session.add(new_user)

            db.session.commit()

            return dict(message=new_user.to_dict(),
                        status_code=201)
        except AssertionError as exception_message:
            return dict(message="%s" % exception_message,
                        status_code=400)

    def add(self, request):
        data = request.get_json()

        if "username" not in data:
            return dict(message="No username provided",
                        status_code=400)

        if "password" not in data:
            return dict(message="No password provided",
                        status_code=400)

        if "email" not in data:
            return dict(message="No email provided",
                        status_code=400)

        try:
            new_user = User(username=data["username"],
                            email=data["email"])

            new_user.set_password(data["password"])

            db.session.add(new_user)

            db.session.commit()

            return dict(message=new_user.to_dict(),
                        status_code=201)
        except AssertionError as exception_message:
            return dict(message="%s" % exception_message,
                        status_code=400)

    def get(self):
        users = User.query.all()

        users_list = [user.to_dict() for user in users]

        return dict(message=users_list, status_code=200)

    def get_by_id(self, id):
        user = User.query.get(id).to_dict()

        if user:
            return dict(message=user, status_code=200)
        else:
            return dict(message="User with ID %s not found" % id,
                        status_code=404)

    def update(self, id, request):
        target_user = User.query.get(id)

        if not target_user:
            return dict(message="User with ID %s not found" % id,
                        status_code=404)

        data = request.get_json()

        try:
            if "email" in data:
                target_user.email = data["email"]

            if "password" in data:
                target_user.set_password(data["password"])

            db.session.commit()

            return dict(message=target_user.to_dict(), status_code=200)
        except AssertionError as exception_message:
            return dict(message="%s" % exception_message,
                        status_code=400)

    def delete(self, id):
        target_user = User.query.get(id).to_dict()

        if not target_user:
            return dict(message="User with ID %s not found" % id,
                        status_code=404)
        else:
            User.query.filter_by(id=id).delete()
            db.session.commit()

            return dict(message=target_user, status_code=200)

from api.models import db
from api.models.user import User


class UserService:
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

        return dict(message=users, status_code=200)

    def get_by_id(self, id):
        user = User.query.filter_by(id=id).first()

        if user:
            return dict(message=user.to_dict(), status_code=200)
        else:
            return dict(message="User with ID %s not found" % id,
                        status_code=404)

import unittest
from api import create_app
from api.models import db
from api.models.user import User
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan', email="susan@example.com")
        u.set_password("Susan1986!")
        self.assertFalse(u.check_password("John1987!"))
        self.assertTrue(u.check_password("Susan1986!"))


if __name__ == '__main__':
    unittest.main(verbosity=2)

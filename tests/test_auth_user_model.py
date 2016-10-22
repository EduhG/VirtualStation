import unittest
from app import create_app, db
from app.auth.models import User, Role, Permission


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # test for non blank passwords
    def test_password_setter(self):
        user = User(password='password')
        self.assertTrue(user.password_hash is not None)

    # test for blank passwords
    def test_no_password_getter(self):
        user = User(password='password')
        with self.assertRaises(AttributeError):
            user.password

    # test password_verification function. decrypted password should match raw password
    def test_password_verification(self):
        user = User(password='password')
        self.assertTrue(user.verify_password('password'))
        self.assertFalse(user.verify_password('password1'))

    # two salted passwords should not match
    def test_password_salts_dont_match(self):
        user = User(password='password')
        user2 = User(password='password')
        self.assertTrue(user.password_hash != user2.password_hash)

    # tests for roles and permissions
    def test_roles_and_permissions(self):
        Role.insert_roles()

        u = User(email='example@example.com', password='password')
        self.assertTrue(u.can(Permission.CHECK_STATUS))
        self.assertFalse(u.can(Permission.MODERATE))


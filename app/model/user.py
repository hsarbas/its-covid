from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """
    Handles users database
    """
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password_hash = None

        self.set_password(password)

    def set_password(self, password):
        """
        Generate and store hashed password
        :param password:
        :return:
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if input password is the same as unhashed password stored in db
        :param password:
        :return:
        """
        return check_password_hash(self.password_hash, password)

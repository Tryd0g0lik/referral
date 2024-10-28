from datetime import datetime

import sqlalchemy as sq

from referral.flasker import bcrypt
from referral.models_more.model_init import Base


# def postman_users(Base):
class Users(Base):
    """This is a model Users of table in db"""

    __tablename__ = "users"

    id = sq.Column(sq.Integer, primary_key=True)
    firstname = sq.Column("user_name", sq.String(50), nullable=False)
    email = sq.Column("email_address", sq.String(50), nullable=False, unique=True)
    password = sq.Column("password", sq.String(150), nullable=False)
    send = sq.Column("sender", sq.Boolean())
    is_activated = sq.Column("is_activated", sq.Boolean())
    is_active = sq.Column("is_active", sq.Boolean())
    date = sq.Column(sq.DateTime, default=datetime.utcnow)
    activation_token = sq.Column(sq.String(255), nullable=True)
    token_created_at = sq.Column(sq.DateTime, nullable=True)

    def __str__(self):
        """How can see a table to the console"""
        return f"User ID: {self.id}, Firstname: {self.firstname}"

    def set_password(self, password: str):
        """Set of password's hash"""
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password: str):
        """Passwords checking"""
        return bcrypt.check_password_hash(self.password, password)

    # return Users

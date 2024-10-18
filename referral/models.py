"""Here is a connection with a db of PostgreSQL"""

import psycopg2

from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER)
from referral.flasker import app_, bcrypt, db


def get_db_connection():
    """Connections with a db"""
    conn = psycopg2.connect(
        dbname=PROJECT_REFERRAL_SETTING_POSTGRES_DB,
        user=PROJECT_REFERRAL_SETTING_POSTGRES_USER,
        password=PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
    )
    return conn


def create_db():
    db = get_db_connection()
    with app_.open_resource("referral_db.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


class Users(db.Model):
    """This is a model Users of table in db"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column("user_name", db.String(50), nullable=False)
    email = db.Column("email_address", db.String(50), nullable=False)
    password = db.Column("password", db.String(50), nullable=False)
    is_activated = db.Column("is_activated", db.Boolean())
    activate = db.Column("activate", db.Boolean())

    def __repr__(self):
        return f"User ID: {self.id}, Firstname: {self.firstname}"

    def set_password(self, password: str):
        """Set of password's hash"""
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password: str):
        """Passwords checking"""
        return bcrypt.check_password_hash(self.password_hash, password)

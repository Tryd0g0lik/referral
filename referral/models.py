"""Here is a connection with a db of PostgreSQL"""

import psycopg2
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String
from flasker import app_, bcrypt

from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER)


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

db = SQLAlchemy(app_)
class Users(db.Model):
    """This is a model Users of table in db"""
    __tablename__ = "users"
    firstname = db.Column("user_name", db.String(50), nullable=False)
    email = db.Column("email_address", db.String(50), nullable=False)
    password = db.Column("password", db.String(50))
    is_activated = db.Column("is_activated", db.Boolean(default=False))
    is_activate = db.Column("activate", db.Boolean(default=False))
    
    def set_password(self, password: str):
        """Set of password's hash"""
        self.password_hash = bcrypt.generate_password_hash(password)\
            .decode('utf-8')
    def check_password(self, password: str):
        """Passwords checking """
        return bcrypt.check_password_hash(
            self.password_hash,
            password
        )
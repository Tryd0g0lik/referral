"""Here is a connection with a db of PostgreSQL"""
from datetime import datetime

import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER,
                     PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PORT)
from referral.flasker import app_, bcrypt, db
metadata_obj = MetaData()


def get_db_connection():
    """Connections with a db"""
    conn = psycopg2.connect(
       app_.config['SQLALCHEMY_DATABASE_URI']
    )
    # conn.row_factory =
    # database = PROJECT_REFERRAL_SETTING_POSTGRES_DB,
    # user = PROJECT_REFERRAL_SETTING_POSTGRES_USER,
    # host = PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
    # port = PROJECT_REFERRAL_SETTING_POSTGRES_PORT,
    # password = PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
    return conn


# def create_db():
#     conn = {}
#     cursor = {}
#     try:
#         conn = get_db_connection()
#         with app_.open_resource('sq_db.sql', mode='r') as f:
#             cursor = conn.cursor().executescript(f.read())
#
#         # sql_create_db = f'create database {PROJECT_REFERRAL_SETTING_POSTGRES_DB}'
#         # cursor.execute(sql_create_db)
#     except (Exception, Error) as err:
#         print(f"[create_db]: ERROR from start app: {err.__str__()}")
#     finally:
#         if conn:
#             conn.commit()
#             conn.close()
#             cursor.close()
#             print("[create_db]: The conaction to PostgreSQL was closed ")
# create_db()

class Users(db.Model):
    """This is a model Users of table in db"""

    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column("user_name", db.String(50), nullable=False)
    email = db.Column("email_address", db.String(50), nullable=False)
    password = db.Column("password", db.String(50), nullable=False)
    is_activated = db.Column("is_activated", db.Boolean())
    activate = db.Column("activate", db.Boolean())
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """How can see a table to the console"""
        return f"User ID: {self.id}, Firstname: {self.firstname}"

    def set_password(self, password: str):
        """Set of password's hash"""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")
        

    def check_password(self, password: str):
        """Passwords checking"""
        return bcrypt.check_password_hash(self.password_hash, password)

"""Here is a connection with a db of PostgreSQL"""
from datetime import datetime
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER,
                     PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PORT)
from .flasker import bcrypt

DSN = f'postgresql://{PROJECT_REFERRAL_SETTING_POSTGRES_USER}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD}@\
{PROJECT_REFERRAL_SETTING_POSTGRES_HOST}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PORT}/\
{PROJECT_REFERRAL_SETTING_POSTGRES_DB}'
engine = sq.create_engine(DSN, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Basic class"""
    pass

class Users(Base):
    """This is a model Users of table in db"""

    __tablename__ = "users"
    
    id = sq.Column(sq.Integer, primary_key=True)
    firstname = sq.Column("user_name", sq.String(50), nullable=False)
    email = sq.Column(
        "email_address",
        sq.String(50), 
        nullable=False,
        unique=True)
    password = sq.Column("password", sq.String(150), nullable=False)
    send = sq.Column("sender",sq.Boolean() )
    is_activated = sq.Column("is_activated", sq.Boolean())
    activate = sq.Column("activate", sq.Boolean())
    date = sq.Column(sq.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     """How can see a table to the console"""
    #     return f"User ID: {self.id}, Firstname: {self.firstname}"
    def __str__(self):
        """How can see a table to the console"""
        return f"User ID: {self.id}, Firstname: {self.firstname}"

    def set_password(self, password: str):
        """Set of password's hash"""
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password: str):
        """Passwords checking"""
        return bcrypt.check_password_hash(self.password, password)

def create_tables(engines):
    try:
        Base.metadata.drop_all(engines)
        print(f"[create_table]: Drop All")
        
        Base.metadata.create_all(engines)
    except Exception as err:
        print(f"[create_table]: Error => {err.__str__()}")
create_tables(engine)

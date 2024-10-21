from datetime import datetime
import sqlalchemy as sq
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from wtforms import StringField

from referral.flasker import bcrypt
from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PORT,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER)
from referral.models_more.model_init import Base

from referral.tokenization import generate_unique_token, \
    generate_unique_referral_code
from typing import Dict, Callable, Any

class Referrals(Base):
    __tablename__ = "referrals"
    
    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(
        sq.Integer,
        ForeignKey('users.id'), unique=True)
    email = relationship(
        "Users",
        backref="referral",
        cascade="all, delete-orphan",
        )
    description = sq.Column("description", sq.String(150), nullable=False)
    referral_code = sq.Column(
        "referral_code",
        sq.String(150),
        nullable=True,
        unique=True)
    is_send = sq.Column("is_send",sq.Boolean())
    is_activated = sq.Column("is_activated", sq.Boolean())
    date = sq.Column(sq.DateTime, default=datetime.utcnow)
    
    def __init__(self, user: Dict[int, object], **kw: Any):
        super().__init__(**kw)
        self.user_id = user['id']
        self.referral_code = generate_unique_referral_code()
    def __str__(self):
        return f"User email: {self.email} Description: "

   
   

from datetime import datetime
from typing import Any, Dict

import sqlalchemy as sq
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from referral.flasker import app_
from referral.interfaces.tokenization import EmailToGenerateToken
from referral.models_more.model_init import Base
e = EmailToGenerateToken(app_)
# cascade="all, delete-orphan",
# def postman_referrals(Base) -> object:
#     """This is a stakeholder"""
class Referrals(Base):
    __tablename__ = "referrals"

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(
        sq.Integer,
        sq.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )
    description = sq.Column("description", sq.String(150))
    
    referral_code = sq.Column(
        "referral_code", sq.String(150), nullable=True, unique=True
    )
    is_send = sq.Column("is_send", sq.Boolean(), default=False)
    is_activated = sq.Column("is_activated", sq.Boolean(), default=False)
    date = sq.Column(sq.DateTime, default=datetime.utcnow)
    
    email = relationship(
        "Users",
        backref="referral"
    )
    
    def __init__(self, user: object, **kw: Any):
        super().__init__(**kw)
        self.user_id = user.id
        self.referral_code = e.generate_dumps_token_len(user.email, 12)

    def __str__(self):
        return f"User email: {self.email} Description: "
    # return Referrals
from datetime import datetime
from typing import Any, Dict

import sqlalchemy as sq
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from referral.flasker import app_
from referral.interfaces.tokenization import EmailToGenerateToken
from referral.models_more.model_init import Base
e = EmailToGenerateToken(app_)
# cascade="all, delete-orphan",

class Referrals(Base):
    __tablename__ = "referrals"

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(
        sq.Integer,
        sq.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )
    email = relationship(
        "Users",
        backref="referral"
    )
    description = sq.Column("description", sq.String(150), nullable=False)
    referral_code = sq.Column(
        "referral_code", sq.String(150), nullable=True, unique=True
    )
    is_send = sq.Column("is_send", sq.Boolean())
    is_activated = sq.Column("is_activated", sq.Boolean())
    date = sq.Column(sq.DateTime, default=datetime.utcnow)

    def __init__(self, user: Dict[int, object], **kw: Any):
        super().__init__(**kw)
        self.user_id = user["id"]
        self.referral_code = e.generate_dumps_token(user["email"])

    def __str__(self):
        return f"User email: {self.email} Description: "

"""This is file has functions to working with referral code."""
from typing import Callable
import bcrypt
from .tokenization import generate_unique_token


def generate_unique_referral_code(func: Callable[[], str]) -> str:
    code = generate_unique_token()

    # HASH
    hashed_code = bcrypt.hashpw(code.encode("utf-8"), bcrypt.gensalt())
    return hashed_code.decode("utf-8")
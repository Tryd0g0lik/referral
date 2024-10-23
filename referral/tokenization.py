"""Here a token generater """

import uuid
from typing import Callable, Dict

import bcrypt

tokens = set()


def generate_unique_token() -> str:
    """
    Here a token generate. It a unique token returning.
    :return: str Exemple '3beeb1f1-2ec2-475e-bd38-4952f2e4235b'
    """
    while True:
        new_token = str(uuid.uuid4())
        if new_token not in tokens:
            tokens.add(new_token)
            return new_token


def generate_unique_referral_code(func: Callable[[], str]) -> str:
    code = generate_unique_token()

    # HASH
    hashed_code = bcrypt.hashpw(code.encode("utf-8"), bcrypt.gensalt())
    return hashed_code.decode("utf-8")


def postman_token(email: str, user: object):
    """
    Token create and sending to the email.
    :param email: str. User's email is addressee.
    :param user: object from the db.
    :return: is empty.
    """
    # AUTHENTICATION FROM THE EMAIL
    token = generate_token(email)
    user.activation_token = token
    user.token_created_at = datetime.utcnow()
    send_activation_email(normalized_email, token)
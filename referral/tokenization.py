"""Here a token generater """

import uuid
from typing import Callable, Dict
from itsdangerous import URLSafeTimedSerializer
import bcrypt

from referral.flasker import app_

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


# https://itsdangerous.palletsprojects.com/en/2.2.x/url_safe/#itsdangerous.url_safe.URLSafeSerializer

class EmailToGenerateToken:
    def __init__(self):
        self.__s = URLSafeTimedSerializer(app_.secret_key)
   
    def generate_dumps_token(self, email: str) -> str:
        return self.__s.dumps(email, salt="email-confirm")
    
    def set_load_token(self, token: str) -> None:
        """
        Token receive to an event point
        :param token: str
        :return:
        """
        self.__token: str = token
    
     
    def get_load_token(self) -> str:
        """
        
        :return: 'email': str
        
        """
        token = self.__s.loads(
            self.__token,
            salt="email-confirm",
            max_age=120)
        return token
    
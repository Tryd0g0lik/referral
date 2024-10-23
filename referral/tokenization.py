"""Here a token generater """

import uuid
from datetime import datetime
from typing import Callable, Dict
from itsdangerous import URLSafeTimedSerializer
import bcrypt

from referral.flasker import app_
from referral.postman.sender import send_activation_email

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

class EmailToGenerateToken:
    """
    This class is a token's generate.
    :param app: object from 'app = Flask(__name__)' for a entrypoint
    """
    def __init__(self, app: type(app_)):
        self.__s = URLSafeTimedSerializer(app.secret_key)
   
    def generate_dumps_token(self, email: str) -> str:
        """
        This is token's generate. In token inserting email.
        :param email: str. Is an user's email.
        :return: token: str
        """
        return self.__s.dumps(email, salt="email-confirm")
    
    def set_load_token(self, token: str) -> None:
        """
        This a method is addition for 'get_load_token'.
        Token receive and data to transform for the private variable.
        :param token: str
        :return:
        """
        self.__token: [str, None] = token
    
     
    def get_load_token(self) -> str:
        """
        This a method is addition for 'set_load_token'
        :return: 'email': str If a time of create is more 120 sec return error.
        """
        token = ''
        token += self.__s.loads(
            self.__token[0:],
            salt="email-confirm",
            max_age=120)
        
        return token



    
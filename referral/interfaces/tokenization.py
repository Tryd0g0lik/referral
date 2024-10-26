"""Here a token generater"""

import uuid
from itsdangerous import URLSafeTimedSerializer

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


class EmailToGenerateToken:
    """
    This class is a token's generate.
    :param app: object from 'app = Flask(__name__)' for a entrypoint.
    Here an email insert in token's and back.
    """
    
    def __init__(self, app: type(app_)):
        self.__s = URLSafeTimedSerializer(app.secret_key)
    
    def generate_dumps_token(self, email: str) -> str:
        """
        This is token's generate. There an Email inserting  token's string.
        :param email: str. Is an user's email.
        :return: token: str
        """
        return self.__s.dumps(email, salt="email-confirm")
    def generate_dumps_token_len(self, email: str, length=150) -> str:
        """
        This is token's generate. There an Email inserting  token's string.
        :param email: str. Is an user's email.
        :param length: int. Default 150.
        :return: token: str
        """
        t = self.__s.dumps(email, salt="email-confirm")
        if length > 150:
            length = 150
        return ''.join(t[ind] for ind in range(0, length))
    
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
            max_age=120
        )
        
        return token




"""Here a token generater """
from typing import Dict, Callable
import uuid
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
   hashed_code = bcrypt.hashpw(
       code.encode('utf-8'),
       bcrypt.gensalt()
   )
   return hashed_code.decode('utf-8')

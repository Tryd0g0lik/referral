"""Here a token generater """

import uuid

tokens = set()


def generate_unique_token():
    """
    Here a token generate. It a unique token returning.
    :return: str Exemple '3beeb1f1-2ec2-475e-bd38-4952f2e4235b'
    """
    while True:
        new_token = str(uuid.uuid4())
        if new_token not in tokens:
            tokens.add(new_token)
            return new_token

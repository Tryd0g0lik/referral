"""Email's message sending to the users email"""

from flask_mail import Message

from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_PORT_TO_BACKEND)
from referral.flasker import mail


def send_activation_email(user_email, token):
    """ "
    Here a message send to the user's Email.
    :param user_email: str. It is addressee.
    :param token: str. Max length is 150 symbols.
    """
    activation_link = f"http://{PROJECT_REFERRAL_SETTING_POSTGRES_HOST}:{PROJECT_REFERRAL_PORT_TO_BACKEND}/activate/{token}"
    try:
        msg = Message(subject="Activate Your Account", recipients=[user_email])
        msg.body = f"Please click the link to activate your account: {activation_link}"
        mail.send(msg)
    except Exception as e:
        print(f"[send_activation_email]: Something what wrong! Error => {e}")

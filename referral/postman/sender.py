from flask_mail import Message
from referral.flasker import mail
from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_HOST)

def send_activation_email(user_email, token):
    activation_link = f"http://{PROJECT_REFERRAL_SETTING_POSTGRES_HOST}:5000/activate/{token}"  # Замените на ваш домен
    msg = Message(subject="Activate Your Account", recipients=[user_email])
    msg.body = f"Please click the link to activate your account: {activation_link}"
    mail.send(msg)
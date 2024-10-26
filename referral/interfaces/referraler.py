"""This is file has functions to working with referral code."""
from typing import Callable
import bcrypt
from .tokenization import generate_unique_token

import random
import string
import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)
def generate_referral_code(length=6):
    """Generate a random referral code."""
    characters = string.ascii_letters + string.digits
    referral_code = ''.join(random.choice(characters) for _ in range(length))
    return referral_code
"""Here data imports from the file '.env' of django project"""

import os

import dotenv

dotenv.load_dotenv()

PROJECT_REFERRAL_SETTING_POSTGRES_DB = os.getenv(
    "PROJECT_REFERRAL_SETTING_POSTGRES_DB", ""
)
PROJECT_REFERRAL_SETTING_POSTGRES_USER = os.getenv(
    "PROJECT_REFERRAL_SETTING_POSTGRES_USER", ""
)
PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD = os.getenv(
    "PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD", ""
)
PROJECT_REFERRAL_SETTING_POSTGRES_HOST = os.getenv(
    "PROJECT_REFERRAL_SETTING_POSTGRES_HOST", ""
)
PROJECT_REFERRAL_SETTING_POSTGRES_PORT = os.getenv(
    "PROJECT_REFERRAL_SETTING_POSTGRES_PORT", ""
)
PROJECT_REFERRAL_SECRET_KEY = os.getenv("PROJECT_REFERRAL_SECRET_KEY", "")
EMAIL_HOST = os.getenv("MAIL_SERVER", "")
EMAIL_PORT = os.getenv("EMAIL_PORT", "")
MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "")
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "")
TOKEN_TIME_MINUTE_EXPIRE = os.getenv("TOKEN_TIME_MINUTE_EXPIRE", "")
PROJECT_REFERRAL_HOST_TO_BACKEND = os.getenv("PROJECT_REFERRAL_HOST_TO_BACKEND", "")
PROJECT_REFERRAL_PORT_TO_BACKEND = os.getenv("PROJECT_REFERRAL_PORT_TO_BACKEND", "")
PROJECT_REFERRAL_PROTOCOL_TO_BACKEND = os.getenv(
    "PROJECT_REFERRAL_PROTOCOL_TO_BACKEND", ""
)

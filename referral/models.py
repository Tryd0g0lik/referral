"""Here is a connection with a db of PostgreSQL"""

import psycopg2

from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER)


def get_db_connection():
    """Connections with a db"""
    conn = psycopg2.connect(
        dbname=PROJECT_REFERRAL_SETTING_POSTGRES_DB,
        user=PROJECT_REFERRAL_SETTING_POSTGRES_USER,
        password=PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
    )
    return conn

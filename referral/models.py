"""Here is a connection with a db of PostgreSQL"""

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from dotenv_ import (PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PORT,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER)
from referral.flasker import app_
from referral.models_more.model_init import Base

DSN = f"postgresql://{PROJECT_REFERRAL_SETTING_POSTGRES_USER}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD}@\
{PROJECT_REFERRAL_SETTING_POSTGRES_HOST}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PORT}/\
{PROJECT_REFERRAL_SETTING_POSTGRES_DB}"
engine = sq.create_engine(DSN, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def create_tables(engines):
    try:
        # Base.metadata.drop_all(engines)
        print(f"[create_table]: Drop All")

        Base.metadata.create_all(engines)
    except Exception as err:
        print(f"[create_table]: Error => {err.__str__()}")


create_tables(engine)

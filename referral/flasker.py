"""Flask application's page"""

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from dotenv_ import (PROJECT_REFERRAL_SECRET_KEY,
                     PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PORT,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER)


def create_flask():
    """
    Here is a basis function of flask. That is start
    :return: app flask
    """
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(__name__)
    # jwt = JWTManager(app)
    app.config["CSRF"] = CSRFProtect(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        f"postgresql:///\
{PROJECT_REFERRAL_SETTING_POSTGRES_USER}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD}@\
{PROJECT_REFERRAL_SETTING_POSTGRES_HOST}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PORT}/\
{PROJECT_REFERRAL_SETTING_POSTGRES_DB}/"
    
    app.config["JWT_COOKIE_SECURE"] = True
    app.config["BCRYPT"] = Bcrypt(app)
    app.config["SECRET_KEY"] = PROJECT_REFERRAL_SECRET_KEY
    bootstrap = Bootstrap(app)
    db = SQLAlchemy(app)
    app.config["DB"] = db
    app.config["BOOTSTRAP"] = bootstrap
    app.config["DATABASE"] = "/tmp/referral.db"
    app.config.update(dict(DATABASE=os.path.join(app.root_path, "referral.db")))
    return app


app_ = create_flask()
csrf = app_.config["CSRF"]
bcrypt = app_.config["BCRYPT"]
db = app_.config["DB"]

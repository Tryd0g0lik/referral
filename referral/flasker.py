"""Flask application's page"""

import os

from flask import Flask, session
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

from dotenv_ import (EMAIL_HOST, EMAIL_PORT, MAIL_DEFAULT_SENDER,
                     MAIL_PASSWORD, MAIL_USE_TLS, MAIL_USERNAME,
                     PROJECT_REFERRAL_SECRET_KEY,
                     PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PORT,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER,
                     PROJECT_REFERRAL_HOST_TO_BACKEND,
                     PROJECT_REFERRAL_PROTOCOL_TO_BACKEND,
                     PROJECT_REFERRAL_PORT_TO_BACKEND
                     )


def create_flask() -> dict:
    """
    Here is a basis function of flask. That is start
    :return: app flask
    """
    app = Flask(__name__, template_folder="templates")
    # Clear session or perform any necessary logout logic
   
    app.config.from_object(__name__)
    # jwt = JWTManager(app)
    csrf = CSRFProtect(app)

    DSN = f"postgresql://{PROJECT_REFERRAL_SETTING_POSTGRES_USER}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD}@\
{PROJECT_REFERRAL_SETTING_POSTGRES_HOST}:\
{PROJECT_REFERRAL_SETTING_POSTGRES_PORT}/\
{PROJECT_REFERRAL_SETTING_POSTGRES_DB}"
    app.config["SQLALCHEMY_DATABASE_URI"] = DSN

    app.config["JWT_COOKIE_SECURE"] = True
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    bcrypt = Bcrypt(app)
    app.config["SECRET_KEY"] = PROJECT_REFERRAL_SECRET_KEY
    bootstrap = Bootstrap(app)

    app.config["BOOTSTRAP"] = bootstrap
    # EMAIL
    app.config["MAIL_SERVER"] = EMAIL_HOST
    app.config["MAIL_PORT"] = EMAIL_PORT
    app.config["MAIL_USE_TLS"] = MAIL_USE_TLS
    app.config["MAIL_USERNAME"] = MAIL_USERNAME
    app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
    app.config["MAIL_DEFAULT_SENDER"] = MAIL_DEFAULT_SENDER
    mail = Mail(app)

    # LOGIN SESSION
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    host = f"{PROJECT_REFERRAL_PROTOCOL_TO_BACKEND}://{PROJECT_REFERRAL_HOST_TO_BACKEND}:{PROJECT_REFERRAL_PORT_TO_BACKEND}"
    # CORS
    CORS(app, resources={r"/api/v1/*": {"origins": host}})

    
    # clear session
    # @app.before_request
    # def clear_session():
    #     session.clear()

    return {
        "app": app,
        "mail": mail,
        "csrf": csrf,
        "bcrypt": bcrypt,
        "login_manager": login_manager,
    }


flask_dict = create_flask()
app_ = flask_dict["app"]
csrf = flask_dict["csrf"]
bcrypt = flask_dict["bcrypt"]
mail = flask_dict["mail"]
login_manager = flask_dict["login_manager"]
app_type = type(app_)
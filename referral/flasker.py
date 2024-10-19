"""Flask application's page"""

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

from dotenv_ import (PROJECT_REFERRAL_SECRET_KEY,
                     PROJECT_REFERRAL_SETTING_POSTGRES_DB,
                     PROJECT_REFERRAL_SETTING_POSTGRES_HOST,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD,
                     PROJECT_REFERRAL_SETTING_POSTGRES_PORT,
                     PROJECT_REFERRAL_SETTING_POSTGRES_USER,
                     EMAIL_HOST,
                     EMAIL_PORT, MAIL_DEFAULT_SENDER,
                     MAIL_USE_TLS, MAIL_USERNAME, MAIL_PASSWORD)









def create_flask():
    """
    Here is a basis function of flask. That is start
    :return: app flask
    """
    app = Flask(__name__, template_folder="templates")

 
   
    app.config.from_object(__name__)
    # jwt = JWTManager(app)
    csrf = CSRFProtect(app)
    # app.config.update(
    #     dict(
    #         DATABASE=os.path.join(
    #             app.root_path,
    #             f"{PROJECT_REFERRAL_SETTING_POSTGRES_DB}.db"
    #         )
    #     )
    # )
    DSN = f'postgresql://{PROJECT_REFERRAL_SETTING_POSTGRES_USER}:\
    {PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD}@\
    {PROJECT_REFERRAL_SETTING_POSTGRES_HOST}:\
    {PROJECT_REFERRAL_SETTING_POSTGRES_PORT}/\
    {PROJECT_REFERRAL_SETTING_POSTGRES_DB}'
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
    
    return {"app": app, "mail": mail, "csrf": csrf, "bcrypt": bcrypt}

flask_dict = create_flask()
app_ = flask_dict["app"]
csrf = flask_dict["csrf"]
bcrypt = flask_dict["bcrypt"]
mail = flask_dict["mail"]



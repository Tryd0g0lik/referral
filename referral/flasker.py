"""Flask application"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_jwt_extended import JWTManager

from referral.tokenization import generate_unique_token

app = Flask(__name__)
jwt = JWTManager(app)

app.config["JWT_COOKIE_SECURE"] = True
app.config["JWT_SECRET_KEY"] = generate_unique_token()
bootstrap = Bootstrap(app)

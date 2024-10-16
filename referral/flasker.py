"""Flask application"""

from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_COOKIE_SECURE"] = True

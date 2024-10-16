from flask import Flask, request
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_COOKIE_SECURE"] = True
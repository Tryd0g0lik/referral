from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager,
                                create_access_token)


app = Flask(__name__)
jwt = JWTManager(app)
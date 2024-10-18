"""Flask application"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_jwt_extended import JWTManager

from referral.tokenization import generate_unique_token
from flask_wtf.csrf import CSRFProtect
from dotenv_ import PROJECT_REFERRAL_SECRET_KEY
app = Flask(__name__, template_folder="templates")
# jwt = JWTManager(app)
csrf = CSRFProtect(app)
# csrf = CSRFProtect()

app.config["JWT_COOKIE_SECURE"] = True
app.config["SECRET_KEY"] = PROJECT_REFERRAL_SECRET_KEY # generate_unique_token()
bootstrap = Bootstrap(app)
# csrf.init_app(app)

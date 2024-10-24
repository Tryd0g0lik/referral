from datetime import datetime
from referral.postman.sender import send_activation_email
from referral.interfaces.tokenization import EmailToGenerateToken


def postman_token(email: str, user: object, app: object) -> str:
    """
    Token create and sending to the email.
    To an entrypoint:
    :param email: str. User's email is addressee.
    :param user: object from the db.
    :param app: object from 'app = Flask(__name__)'
    :return: str.
    """
    g = EmailToGenerateToken(app)
    token = g.generate_dumps_token(email)
    user.activation_token = token
    user.token_created_at = datetime.utcnow()
    send_activation_email(email, token)
    return token
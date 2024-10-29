"""
Flask form for page registration
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

from referral.forms.validators import validate_emails


class GetFormAuthorization(FlaskForm):
    """
    This is a form under dashbord of profile's page.
    It's "Создать referral code".
    :param 'email': str. User's email for profile's activation.
    :param 'password': str. User's password for profile's activation.
    """

    email = StringField(
        "email",
        validators=[
            validators.DataRequired(),
            validators.Email(),
        ],
    )
    password = StringField(
        "password",
        validators=[
            validators.InputRequired(),
            validators.length(min=3, message="Min. (Количество символов) 3."),
        ],
    )

    submit = SubmitField("Login", render_kw={"class": "btn btn-secondary"})

    def validator_register_email(self, email: str) -> [str, bool]:
        """
        This is a email's validator.
        :param email: str. Min. Length is 7 symbols.
        :return: str if is all Ok and False if what wrong.
        """
        strBool = validate_emails(email)
        return strBool
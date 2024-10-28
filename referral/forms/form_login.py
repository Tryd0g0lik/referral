"""
Flask form for page registration
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


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

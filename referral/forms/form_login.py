from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

from referral.forms.form_registration import GetFormRegistration


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
            validators.InputRequired(),
            validators.Email(),
            validators.DataRequired(),
        ],
    )
    password = StringField(
        "password",
        validators=[
            validators.InputRequired(),
            validators.length(min=3, message="Min. (Количество символов) 3."),
        ],
    )

    submit = SubmitField("LoginIn", render_kw={"class": "btn btn-secondary"})

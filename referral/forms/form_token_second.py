"""
This a page contain the form model.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

from referral.forms.validators import validate_emails


class GetFormForToken(FlaskForm):
    """
    This a form for send the token. This token
    for repeat send's token!
    :param 'email': str. User's email is addressee.
    """

    email = StringField(
        "email",
        validators=[
            validators.InputRequired(),
            validators.Email(),
            validators.DataRequired(),
        ],
    )

    submit = SubmitField("Make", render_kw={"class": "btn btn-secondary"})

    def validator_register_email(self, email) -> [str, bool]:
        """
        This is a email's validator.
        :param email: str. Min. Length is 7 symbols.
        :return: str if is all Ok and False if what wrong.
        """
        strBool = validate_emails(email)
        return strBool

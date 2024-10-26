from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

from referral.forms.validators import validate_emails


class GetFormReferralCode(FlaskForm):
    """
    This is a form under dashbord of profile's page.
    It's "Создать referral code".
    :param 'email': str. User's email is addressee.
    :param 'description' This a description into the range of 0 to 150 symbol.
    It's a marker for a referral-code.
    """
    #
    # email = StringField(
    #     "email",
    #     validators=[
    #         validators.InputRequired(),
    #         validators.Email(),
    #         validators.DataRequired(),
    #     ],
    # )
    description = StringField(
        "Описание",
        validators=[
            validators.length(
                max=150,
                message="Max. (количество для описания ссылки) 150 символов.",
            ),
        ],
    )
    submit = SubmitField("Make", render_kw={"class": "btn btn-secondary"})
    
    def validator_register_email(self, email: [dict, object]):
        """
        This is a email's validator.
        :param email: [dict, object]. 'main = {"data": "your@mail.ru"}'
        Min. Length is 7 symbols.
        :return: str if is all Ok and False if what wrong.
        """
        strBool = validate_emails(email)
        return strBool
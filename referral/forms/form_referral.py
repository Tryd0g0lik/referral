from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    validators
)

class GetFormReferralCode(FlaskForm):
    email = StringField(
        "email",
        validators=[
            validators.InputRequired(),
            validators.Email(),
            validators.DataRequired()
        ],
        
    )
    description = StringField(
        "Описание",
        validators=[
            validators.length(
                max=150,
                message="Max. (количество для описания ссылки) 150 символов.",
            ),
        ],
    )
    submit = SubmitField("Make", render_rw={"class": "btn btn-secondary"})

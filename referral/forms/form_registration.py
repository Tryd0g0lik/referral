from wtforms import BooleanField,  StringField, SubmitField, validators
from flask_wtf import FlaskForm


class GetFormRegistration(FlaskForm):
    is_activated = BooleanField(
        "Активирован",
        default=False,
        validators=[
            validators.Optional(),
        ],
    )
    is_activate = BooleanField(
        "Активный", default=False, validators=[validators.Optional()]
    )
    firstname = StringField(
        "Имя пользователя",
        validators=[
            validators.InputRequired(),
            validators.length(
                min=4,
                max=50,
                message="Min. (Количество символов) 4, Max. (количество символов) 50.",
            ),
        ],
    )
    
    email = StringField(
        "Email",
        validators=[
            validators.InputRequired(),
            validators.Email()
        ]
    )
    
    password = StringField(
        "Password",
        validators=[
            validators.InputRequired(),
            validators.Length(min=3, message="Min. (Количество символов) 3."),
        ],
    )
    password2 = StringField(
        "Password2",
        validators=[
            validators.InputRequired(),
            validators.length(min=3, message="Min. (Количество символов) 3."),
        ],
    )
    submit = SubmitField(
        "Регистрировать",
        render_kw={'class': "btn btn-secondary"}
    )


 

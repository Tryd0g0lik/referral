"""Here a router of the flask app."""

from cfgv import ValidationError
from flask import (jsonify, redirect, render_template, request,  # jsonify,
                   url_for)

# from flask_jwt_extended import create_access_token
from referral.flasker import app_, csrf
from referral.forms.form_registration import GetFormRegistration
from referral.models import Users, db, get_db_connection


def app_router():
    """Total function"""

    @app_.route(
        "/",
        methods=[
            "GET",
            "POST",
        ],
    )
    def upload_main_page():
        """
        Here is a main page uploading
        :return:
        """
        if request.method == "GET":
            pass
        elif request.method == "POST":
            # Предположим, что вы получаете данные из формы
            # Преобразование данных формы в словарь
            # params = request.form.to_dist()
            pass
        return render_template(
            "index.html",
        )

    @app_.route(
        "/register",
        methods=["GET", "POST"],
    )
    @csrf.exempt
    async def register():
        # Логика регистрации пользователя
        form = GetFormRegistration()
        conn = get_db_connection()
        error = "some_view"
        if request.method == "POST" and form.validate_on_submit():
            try:
                # Pass the form's email field
                normalized_email = form.validate_email(form.email)
                firstname = form.firstname.data
                password = form.password.data
                password2 = form.password2.data
                # Проверка на пустой пароль
                if not password:
                    return render_template(
                        "users/register.html",
                        form=form,
                        error="Password cannot be empty.",
                    )

                if password != password2:
                    return render_template(
                        "users/register.html",
                        form=form,
                        error="Passwords do not match.",
                    )
                
                new_user = Users()
                new_user.firstname=firstname
                new_user.set_password(password)

                conn.execute(
                    Users.__table__.insert().values(
                        firstname=new_user.firstname,
                        email=normalized_email,
                        password = new_user.password,
                        is_activated=False,
                        activate=False
                    )
                )
                
                conn.session.commit()
                return redirect(url_for("some_view"))
            except ValidationError as e:
                # Lower is a roll back if received the error.
                error = "some_view" + str(e)
                conn.rollback()
                
            finally:
                conn.close()
                print(f"ERRR: {error}")
                return render_template("users/register.html",
                                       form=form,
                                       error=error)
                
        elif not form.validate_on_submit():
            return render_template("users/register.html", form=form)
        
        return render_template("users/register.html", form=form)
        # response = render_template(render_template("users/register.html"))
        # return render_template("users/register.html", form=form)

    @app_.route(
        "/login",
        methods=[
            "GET",
            "POST",
        ],
    )
    async def login():
        # Логика аутентификации пользователя
        if request.method == "POST":
            firstname = request.form["firstname"]
            password = request.form["password"]
            user = Users.query.filter_by(firstname=firstname).first()
            # Сравниваем хеши
            if user and Users.check_password(password):
                return "login successful!"
            else:
                return "Invalid username or password"
        # Проверка пользователя и создание токена
        # access_token = create_access_token(identity=firstname)
        return jsonify(access_token="data")

    # @app_.route(
    #     "/registrator",
    #     methods=[
    #         "POST",
    #     ],
    # )
    # async def login():
    # Логика аутентификации пользователя
    # username = await request.json.get("username")
    # email = await request.json.get("email")
    # Проверка пользователя и создание токена
    # access_token = create_access_token(identity=username)

    # return jsonify(access_token=access_token)

    # @app_.route("/referal_code", methods=["POST"])
    # @jwt_required()
    # async def create_referral_code():
    #     # Логика создания реферального кода
    #     pass
    #
    # @app_.route("/referrals/<referrer_id>", methods=["GET"])
    # @jwt_required()
    # async def get_referrals(referral_id):
    #     # Логика получения рефералов
    #     pass

    return app_

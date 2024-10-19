"""Here a router of the flask app."""
from datetime import datetime

from cfgv import ValidationError
from flask import (jsonify, redirect, render_template, request,  # jsonify,
                   url_for)

# from flask_jwt_extended import create_access_token
from referral.flasker import app_, csrf
from referral.forms.form_registration import GetFormRegistration
from .models import Users, Session

from itsdangerous import URLSafeTimedSerializer
from itsdangerous import URLSafeTimedSerializer
from flask import redirect, url_for, flash
from .postman.sender import send_activation_email

s = URLSafeTimedSerializer(app_.secret_key)

def generate_token(email):
    return s.dumps(email, salt='email-confirm')
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
        
        error = "some_view"
        sess = Session()
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
                password_hash = new_user.password_hash

                user = Users(
                    firstname=new_user.firstname,
                    email=normalized_email,
                    password=password_hash,
                    send=True,
                    is_activated=False,
                    activate=False,
                )
                
                sess.add(user)
                sess.commit()
                error = "OK"
                # AUTHENTICATION FROM THE EMAIL
                token = generate_token(normalized_email)
                send_activation_email(normalized_email, token)
                
            except (Exception, ValidationError) as e:
                # Lower is a roll back if received the error.
                error = "some_view: " + str(e)
                sess.rollback()
                
            finally:
                sess.close()
                print(f"MESSAGE: {error}")
                return render_template("users/register.html",
                                       form=form,
                                       error=error, title="Регистрация")
                
        elif not form.validate_on_submit():
            return render_template("users/register.html", form=form,
                                   title="Регистрация")
        
        return render_template("users/register.html", form=form,
                               title="Регистрация")
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
        
          
        return render_template("users/login.html", title="Авторизация")

    @app_.route(
        "/activate/<token>",
        methods=[
            "GET",
        ],
    )
    async def activate(token):
        """This is activate function"""
        sess = Session()
        
        try:
            # Логика декодирования токена и активации аккаунта
            email = s.loads(
                token, salt='email-confirm', max_age=3600
                )  # Пример декодирования
            user = sess.query(Users).filter_by(email=email).first()
            # user = Users.query.filter_by(email=email).first()
            
            if user:
                user.is_activated = True  # Активируем пользователя
                sess.commit()
                flash(
                    'Your account has been activated! You can now log in.',
                    'success'
                    )
            else:
                flash('Invalid activation token.', 'danger')
                return redirect(
                    url_for('login')
                    )  # Переадресация на страницу входа
        
            return redirect(
                url_for('login')
                )  # Переадресация после успешной активации
    
        except Exception as e:
            print(f"[activate]: Error => {e.__str__()}")
            flash('The activation link is invalid or has expired.', 'danger')
            return redirect(
                url_for('login')
                )  # Переадресация на страницу входа
           
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

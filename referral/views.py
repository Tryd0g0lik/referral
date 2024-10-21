"""Here a router of the flask app."""

from datetime import datetime, timedelta

from cfgv import ValidationError
from flask import (flash, redirect, render_template, request,  # jsonify,
                   url_for)
from flask_login import login_required, login_user
from itsdangerous import URLSafeTimedSerializer

from dotenv_ import TOKEN_TIME_MINUTE_EXPIRE
from referral.flasker import app_, csrf, login_manager
from referral.forms.form_registration import GetFormRegistration

from .forms.form_login import GetFormAuthorization
from .models import Session
from .models_more.model_users import Users

from .postman.sender import send_activation_email
from .user_login import UserLogin

# URL-TOKEN
s = URLSafeTimedSerializer(app_.secret_key)
def generate_token(email):
    return s.dumps(email, salt="email-confirm")


def app_router():
    """Total function"""

    def delete_old_users():
        """Here  all tokens we delete where token time was expired"""
        sess = Session()
        try:
            threshold_time = datetime.utcnow() - timedelta(
                minutes=int(TOKEN_TIME_MINUTE_EXPIRE)
            )
            old_users = (
                sess.query(Users).filter(Users.token_created_at < threshold_time).all()
            )

            if len(old_users) > 0:
                for user in old_users:
                    sess.delete(user)
                print("[delete_old_users]: Now the  old users all was removed")
            else:
                print(f"[delete_old_users]: Here not found the old users")

        except Exception as err:
            print(f"[delete_old_users]: Error => {err.__str__()}")
        finally:
            sess.commit()
            sess.close()

    @app_.route(
        "/",
        methods=[
            "GET",
            "POST",
        ],
    )
    async def upload_main_page():
        """
        Here is a main page uploading
        :return:
        """
        if request.method == "GET":
            # Удаляем users которые просрочили подтверждение email через
            # ссылку-токен на почте.
            delete_old_users()
            pass
        elif request.method == "POST":
            # Предположим, получаем данные из формы
            # Преобразование данных формы в словарь
            # params = request.form.to_dist()
            pass
        return render_template("index.html", message=None)
    
    # USER ACCOUNT
    @app_.route(
        "/register",
        methods=["GET", "POST"],
    )
    @csrf.exempt
    async def register():
        """
        With a function will run when we open the page. This page has a form
        for registrations event
        :return:
        """
        # Logic - registration
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
                # Check a field empty
                if not password:
                    return render_template(
                        "users/register.html",
                        form=form,
                        message="Password cannot be empty.",
                       
                    )

                if password != password2:
                    return render_template(
                        "users/register.html",
                        form=form,
                        message="Passwords do not match.",
                    )

                new_user = Users()
                new_user.firstname = firstname
                new_user.set_password(password)
                password_hash = new_user.password_hash

                user = Users(
                    firstname=new_user.firstname,
                    email=normalized_email,
                    password=password_hash,
                    send=True,
                    is_activated=False,
                    is_active=False,
                )

                # AUTHENTICATION FROM THE EMAIL
                token = generate_token(normalized_email)
                if normalized_email:
                    user.activation_token = token
                    user.token_created_at = datetime.utcnow()
                    send_activation_email(normalized_email, token)
                    error = "OK"
                else:
                    error = "NOT OK"
                sess.add(user)
                sess.commit()

            except (Exception, ValidationError) as e:
                # Lower is a roll back if received the error.
                error = "some_view: " + str(e)
                sess.rollback()

            finally:
                sess.close()
                print(f"MESSAGE: {error}")
                return render_template(
                    "users/register.html",
                    form=form,
                    error=error,
                    title="Регистрация",
                    message=None,
                )

        elif not form.validate_on_submit():
            return render_template(
                "users/register.html",
                form=form,
                title="Регистрация",
                message=None,
            )

        return render_template(
            "users/register.html",
            form=form,
            title="Регистрация",
            message=None,
        )

    @app_.route(
        "/login",
        methods=["GET", "POST"],
    )
    async def login():
        """Opening a page of authorization"""
        # AUTHENTIFICATION logic
        # greate a form
        form_loginin = GetFormAuthorization()
        sess = Session()

        message = None
        if request.method == "POST":
            if form_loginin.validate_on_submit():
                # Received data for a authorization
                email = form_loginin.email.data
                password = form_loginin.password.data
                user = sess.query(Users).filter_by(email=email).first()

                """
                    На каком этапе лучше создавать хеш-пароль???
                    Хешировать email или нет???
                """

                # Below comparing and checking the email and password
                """
                    Сравнение проводить лучше в состоянии хеша или
                    декодировать пароль, затем сравнивать???
                """
                if (user.email == email) and (user.check_password(password)):
                    # Make data to the profiles page
                    userlogin = UserLogin()
                    userlogin.create(user)
                    userlogin.is_authenticated()
                    userlogin.is_anonymous()
                    userlogin.is_active()
                    userlogin.get_id()
                    login_user(userlogin)
                    # Change data from db of the single user
                    user.is_active = True
                    sess.commit()
                    sess.close()
                    message = "Invalid username or password"
                    return redirect(
                        url_for("profiles", title="Profile", message=message)
                    )
                sess.close()
                return render_template(
                    "users/login.html",
                    title="Авторизация",
                    form=form_loginin,
                    message="login successful!",
                )

        elif request.args.get("token") and len(request.args.get("token")) > 10:
            try:
                user = (
                    sess.query(Users)
                    .filter_by(activation_token=request.args.get("token"))
                    .first()
                )
                if user:

                    login_user(user)
                else:
                    message = f"[login]: User invalid"
            except Exception as err:
                message = f"[login]: Token invalid => {err.__str__()}"
            finally:
                sess.commit()
                sess.close()

        return render_template(
            "users/login.html",
            title="Авторизация",
            form=form_loginin,
            message=message,
        )

    @app_.route(
        "/activate/<token>",
        methods=[
            "GET",
        ],
    )
    async def activate(token):
        """This is activation function"""
        sess = Session()

        try:
            # LOGIC DECODE a token
            email = s.loads(token, salt="email-confirm", max_age=120)
            user = sess.query(Users).filter_by(email=email).first()

            # LOGIC a USER ACTIVATION
            if user and user.activation_token == token:
                if user.token_created_at and (
                    datetime.utcnow() - user.token_created_at
                ) < timedelta(minutes=int(TOKEN_TIME_MINUTE_EXPIRE)):

                    # Delete a token time
                    user.token_created_at = None
                    # User activation
                    user.is_activated = True
                    flash(
                        "Your account has been activated! You can now log in.",
                        "success",
                    )

                else:
                    flash("Invalid activation token.", "danger")
                    # Redirecting to an activation/authorization page
                    return redirect(url_for("login"))
            else:
                # Here, a Token is can not find and we make redirect
                flash("Token not found", "danger")
                return redirect(url_for("login"))
            # Redirect when a successful activate
            return redirect(url_for("login", token=token))

        except Exception as e:
            print(f"[activate]: Error => {e.__str__()}")
            flash("The activation link is invalid or has expired.", "danger")
            return redirect(url_for("login"))
        finally:
            sess.commit()
            sess.close()
    
    # PROFILE
    @app_.route(
        "/profile",
        methods=[
            "GET",
        ],
    )
    @login_required
    async def profiles():
        """Opening a page for the user authorized
        This present a list of referral-code"""
        message = "Profile"
        GetFormAuthorization()

        return render_template("users/profile.html", title="Dashboard", message=message)

    
    @app_.route(
        "/profile/add",
        methods=[
            "GET",
            "POST"
        ]
    )
    @login_required
    async def referral_create():
        """This present a list of referral-code"""
        message = "OK"
        return render_template(
            "users/referral_code.html",
            title="Создать referral code",
            form=None,
            message=message,
        )
    
    @app_.route(
        "/profile/delete",
        methods=[
            "GET", "POST"
        ]
    )
    @login_required
    async def referral_delete():
        """This present a list of referral-code"""
        pass
    
    @app_.route(
        "/profile/delete",
        methods=[
            "GET", "POST"
        ]
    )
    @login_required
    async def referral_change():
        """This present a list of referral-code"""
        pass
    
    return app_


# FROM THE lOGINMANAGER
@login_manager.user_loader
def load_user(user_id) -> [object, dict]:
    """
    This is a loader/ Here a loader logic for the
    one user of db.
    :param user_id:str:
    :return:
    """
    from .models import Session, Users
    from .user_login import UserLogin

    sess = Session()
    user = sess.query(Users).filter_by(id=int(user_id)).first()
    userlogin = UserLogin()
    userlogin.create(user)
    userlogin.fromDB(userlogin.get_id())
    sess.close()

    return userlogin

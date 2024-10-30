"""Views of account"""

from datetime import datetime, timedelta

from cfgv import ValidationError
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user

# ENVIRONMENT
from dotenv_ import TOKEN_TIME_MINUTE_EXPIRE
# LOCAL LIB
# URL-TOKEN
from referral.flasker import app_type, csrf
from referral.forms.form_login import GetFormAuthorization
from referral.forms.form_registration import GetFormRegistration
from referral.forms.form_token_second import GetFormForToken
from referral.interfaces.files import receive_pathname_js_file
from referral.interfaces.referraler import generate_referral_code
from referral.interfaces.tokenization import EmailToGenerateToken
from referral.interfaces.user_login import UserLogin
from referral.models import Session
from referral.models_more.model_users import Users
from referral.postman.postman_tokens import postman_token


async def views_accouts(app_) -> app_type:
    """
    Parent for account's interface.
    :param app_: This is a flask's app
    :return: app_
    """
    
    def register_new_user(form, js_file_name, post=True):
        """
        This is sub-function.
        This a function is working by request the 'POST' when user
         pass registration.
        And, a 'GET' when user pass registration by referral code/
        :param form: object of form.
        :param js_file_name: JS's file name.
        :param post: boolean/ If a True - this means a request 'POST', was.
        And a 'False'.
        :return: user: object
        """
        # Pass the form's email field
        class Email:
            """Заглушка"""
            def __init__(self, email):
                self.data = email
        email = Email("new_user@mail.ru")
        strBool = form.validator_register_email(email)
        if post:
            strBool = form.validator_register_email(form.email)
        if type(strBool) == bool:
            return render_template(
                "users/register.html",
                form=form,
                message="Your email address did not go checking!",
                js_file_name=js_file_name,
            )
        # copy
        normalized_email = strBool[0:]
    
        new_user = Users()
        firstname = "Newuser"
        password = generate_referral_code(5)
        password2 = password
        if post:
            password = form.password.data
            firstname = form.firstname.data
            password2 = form.password2.data
        
            
        if password != password2:
                return render_template(
                    "users/register.html",
                    form=form,
                    message="Passwords do not match.",
                    # Below, receive the JS file name.
                    js_file_name=js_file_name,
                )
        new_user.firstname = firstname
    
        # Check a field empty
        if not password:
            return render_template(
                "users/register.html",
                form=form,
                message="Password cannot be empty.",
                js_file_name=js_file_name,
            )
        password_hash = password
        if post:
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
    
        if normalized_email and post:
            # First sending the token to the user's email. This an event
            # when user itself beginning registration.
            postman_token(normalized_email, user, app_)
            error = "OK"
        else:
            error = "NOT OK"
        return user
    # s = URLSafeTimedSerializer(app_.secret_key)
    #
    # def generate_token(email: str) -> str:
    #     return s.dumps(email, salt="email-confirm")

    # USER ACCOUNT
    @app_.route(
        "/register",
        methods=["GET", "POST"],
    )
    @csrf.exempt
    async def register():
        """
        With a function will run when we open the page. This page has a form
        for registrations event.
        :return:
        """
        # Logic - registration
        form = GetFormRegistration()
        # Below, receive the JS file name.
        js_file_name = receive_pathname_js_file()
        error = "some_view"
        sess = Session()
        if request.method == "POST" and form.validate_on_submit():
            try:
                user = register_new_user(form, js_file_name)
                sess.add(user)
                sess.commit()

            except (Exception, ValidationError) as e:
                # Lower is a roll back if received the error.
                error = "some_view: " + str(e)
                sess.rollback()

            finally:
                sess.close()
                print(f"MESSAGE: {error}")
                # Below, receive the JS file name.
                js_file_name = receive_pathname_js_file()
                return render_template(
                    "users/register.html",
                    form=form,
                    error=error,
                    title="Регистрация",
                    message=None,
                    js_file_name=js_file_name,
                )

        elif not form.validate_on_submit():

            return render_template(
                "users/register.html",
                form=form,
                title="Регистрация",
                message=None,
                js_file_name=js_file_name,
            )

        return render_template(
            "users/register.html",
            form=form,
            title="Регистрация",
            message=None,
            js_file_name=js_file_name,
        )

    @app_.route(
        "/login",
        methods=["GET", "POST"],
    )
    @csrf.exempt
    async def login():
        """Opening a page of authorization"""
        # AUTHENTIFICATION logic
        # create a form
        form_loginin = GetFormAuthorization()
        sess = Session()
        # Below, receive the JS file name.
        js_file_name = receive_pathname_js_file()
        message = None
        if request.method == "POST":
            if form_loginin and form_loginin.validate_on_submit():
                try:
                    # Received data for a authorization
                    email = form_loginin.email.data
                    password = form_loginin.password.data
                    user = sess.query(Users).filter_by(email=email).first()
                     # Below comparing and checking the email and password
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
                        # for_cookie_data = user.activation_token
                        data_number = user.id

                        sess.commit()
                        sess.close()
                        message = "login successful!"

                        return redirect(
                            url_for(
                                "profiles",
                                title="Profile",
                                message=message,
                                data_number=data_number
                            )
                        )

                except Exception as e:
                    message = "Invalid username or password"
                    return render_template(
                        "users/login.html",
                        title="Авторизация",
                        form=form_loginin,
                        message=message,
                        js_file_name=js_file_name,
                    )
                finally:
                    sess.close()
            elif not form_loginin.validate_on_submit():
                print(f"[login]: Not validate_on_submit => {form_loginin.errors}")

        elif request.args.get("token"):
            # Below? for a referral's users
            # 12 it is a pseudo password
            if len(request.args.get("token")) <= 12:
                if request.method == "GET":
                    # This is a registration's process of referral's user
                    user_all = sess.query(Users)\
                        .filter_by(activation_token=request.args.get("token"))\
                        .all()
                    user = register_new_user(form_loginin, js_file_name, False)
                    user.is_activated = True
                    user.activation_token = request.args.get("token")
                    user.is_active = True
                    user.date = datetime.utcnow()
                    user.id = (len(list(user_all)) + 1)
                    sess.add(user)
                    sess.commit()
                    # Message is make to the browser
                    message = f" Login {user.email} & password {user.password}"
            try:
                # activation of referral's user
                user = (
                    sess.query(Users).filter_by(activation_token=request.args.get("token")).first()
                )
                if user:
                    userlogin = UserLogin()
                    userlogin.create(user)
                    userlogin.is_authenticated()
                    userlogin.is_anonymous()
                    userlogin.is_active()
                    userlogin.get_id()
                    login_user(userlogin)
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
            js_file_name=js_file_name,
        )

    @app_.route(
        "/activate/<token>",
        methods=["GET", "POST"],
    )
    async def activate(token):
        """
        This an activation function is run when address's row received URL.
        It is '< your_domen>.ru/activate/< token_from_email >'
        :param token: str. 120 second It is his lifetime.
        :return: redirect
        """
        sess = Session()

        try:
            # LOGIC DECODE a token
            g = EmailToGenerateToken(app_)
            g.set_load_token(token)
            email = g.get_load_token()
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

    @app_.route(
        "/repeat_token",
        methods=["POST", "GET"],
    )
    @csrf.exempt
    async def repeat_token():
        """
        This an activation function is run when we fill the line from
        form 'GetFormForToken' and push a submit.
        
        Our token is making send (re-sending) to the email of user.
        :return: redirect or render_template.
        """
        sess = Session()
        form = GetFormForToken()

        # Below, receive the pathname to the JS file.
        js_file_name = receive_pathname_js_file()
        try:
            if request.method == "POST" and form.validate_on_submit():
                # Pass the form's email field
                strBool = form.validator_register_email(form.email)
                if type(strBool) == bool:
                    return render_template(
                        "users/register.html",
                        form=form,
                        message="Your email address did not passed check!",
                        js_file_name=js_file_name,
                    )
                normalized_email = strBool[0:]

                # Look up user in db
                user = sess.query(Users).filter_by(email=normalized_email).first()
                if user:
                    # First sending the token to the user's email.
                    # This an event when user itself beginning registration.
                    token = postman_token(normalized_email, user, app_)

                    # Upgrade the token's data in db.
                    # token time
                    user.token_created_at = datetime.utcnow()
                    # User activation token
                    user.activation_token = token
                    flash(
                        """The activation link to the emil It
                        is running only two minutes.""",
                        "success",
                    )
                    sess.commit()
                    return redirect(url_for("login"))
                else:
                    # Here, a Token is can not be generated.
                    flash(
                        """Generate an activation's token invalid!
Check the email or send the message to support.""",
                        "danger",
                    )
                    return redirect(url_for("register"))
            elif request.method == "GET":
                message = "Повторить токен"
                return render_template(
                    "users/token_repeat.html",
                    title="Повторить токен",
                    form=form,
                    message=message,
                    js_file_name=js_file_name,
                )
        except Exception as e:
            print(f"[repeat_token]: Error => {e.__str__()}")
            flash("The activation link is invalid or has expired.", "danger")

        finally:
            sess.close()

    return app_

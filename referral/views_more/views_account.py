"""Views of account"""
from datetime import datetime, timedelta

from cfgv import ValidationError
from flask import (flash, redirect, render_template, request,  # jsonify,
                   url_for)
from flask_login import login_user
from itsdangerous import URLSafeTimedSerializer
# URL-TOKEN
from referral.flasker import csrf
from referral.forms.form_token_second import GetFormForToken
from referral.postman.postman_tokens import postman_token
from referral.tokenization import EmailToGenerateToken
from referral.user_login import UserLogin
# ENVIRONMENT
from dotenv_ import TOKEN_TIME_MINUTE_EXPIRE
# LOCAL LIB
from referral.flasker import app_type
from referral.forms.form_registration import GetFormRegistration
from referral.forms.form_login import GetFormAuthorization
from referral.models import Session
from referral.models_more.model_users import Users
# from referral.postman.sender import send_activation_email



async def views_accouts(app_) -> app_type:
    """
    Parent for account's interface.
    :param app_: This is a flask's app
    :return: app_
    """
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
                
                strBool = form.validator_register_email(form.email)
                if type(strBool) == bool:
                    return render_template(
                        "users/register.html",
                        form=form,
                        message="Your email address did not go checking!",
                    )
                normalized_email = strBool[0:]
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
                
              
                if normalized_email:
                    # First sending the token to the user's email. This an event
                    # when user itself beginning registration.
                    postman_token(normalized_email, user, app_)
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
    @csrf.exempt
    async def login():
        """Opening a page of authorization"""
        # AUTHENTIFICATION logic
        # greate a form
        form_loginin = GetFormAuthorization()
        sess = Session()
        
        message = None
        if request.method == "POST":
            if form_loginin and form_loginin.validate_on_submit():
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
            elif not form_loginin.validate_on_submit():
                print(f"[login]: Not validate_on_submit => {form_loginin.errors}")
        
        elif request.args.get("token") and len(request.args.get("token")) > 10:
            try:
                user = (
                    sess.query(Users)
                    .filter_by(activation_token=request.args.get("token"))\
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
            "GET", "POST"
        ],
    )
    async def activate(token):
        """This is activation function"""
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
        methods=[
            "POST", "GET"
        ],
    )
    @csrf.exempt
    async def repeat_token():
        """This is activation function"""
        sess = Session()
        form = GetFormForToken()
        message = None
        try:
            if request.method == "POST": #  and form.validate_on_submit():
                # Pass the form's email field
                strBool = form.validator_register_email(form.email)
                if type(strBool) == bool:
                    return render_template(
                        "users/register.html",
                        form=form,
                        message="Your email address did not passed check!",
                    )
                normalized_email = strBool[0:]
                
                # Look up user in db
                user = sess.query(Users).filter_by(email=normalized_email)\
                    .first()
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
                    return redirect(url_for(
                            "login"
                        )
                    )
                else:
                    # Here, a Token is can not be generated.
                    flash("""Generate an activation's token invalid!
Check the email or send the message to support.""", "danger")
                    return redirect(url_for("register"))
            elif request.method == "GET":
                message = "Повторить токен"
                return render_template(
                    "users/token_repeat.html",
                    title="Повторить токен",
                    form=form,
                    message=message,
                )
        except Exception as e:
            print(f"[repeat_token]: Error => {e.__str__()}")
            flash("The activation link is invalid or has expired.", "danger")
            
        finally:
            sess.close()
            
    return app_

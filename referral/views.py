"""Here a router of the flask app."""
from datetime import datetime, timedelta

from cfgv import ValidationError
from flask import (jsonify, redirect, render_template, request,  # jsonify,
                   url_for)
from flask_login import (LoginManager,
                         UserMixin,
                         login_user,
                         login_required,
                         logout_user, current_user)
# from flask_jwt_extended import create_access_token
from referral.flasker import app_, csrf
from referral.forms.form_registration import GetFormRegistration
from .forms.form_login import GetFormAuthorization
from .models import Users, Session

from itsdangerous import URLSafeTimedSerializer
from flask import redirect, url_for, flash
from .postman.sender import send_activation_email
from dotenv_ import TOKEN_TIME_MINUTE_EXPIRE

s = URLSafeTimedSerializer(app_.secret_key)
login_manager = LoginManager()
login_manager.init_app(app_)
def generate_token(email):
    return s.dumps(email, salt='email-confirm')
def app_router():
    """Total function"""

    def delete_old_users():
        """Here  all tokens we delete where token time was expired"""
        sess = Session()
        try:
            threshold_time = datetime.utcnow() - timedelta(
                minutes=int(TOKEN_TIME_MINUTE_EXPIRE)
            )
            old_users = sess.query(Users).filter(
                Users.token_created_at < threshold_time
            ).all()
            
            if len(old_users) > 0:
                for user in old_users:
                    sess.delete(user)
                print("[delete_old_users]: Now the  old users all was removed")
            else:
                print(
                    f"[delete_old_users]: Here not found the old users"
                    )
            
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
            # Предположим, что вы получаете данные из формы
            # Преобразование данных формы в словарь
            # params = request.form.to_dist()
            pass
        return render_template(
            "index.html",
            current_users=None,
            message=None
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
                        message="Password cannot be empty.",
                        current_users=None,
                    )

                if password != password2:
                    return render_template(
                        "users/register.html",
                        form=form,
                        current_users=None,
                        message="Passwords do not match.",
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
                
                # sess.add(user)
                # sess.commit()
                # error = "OK"
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
                return render_template("users/register.html",
                                       form=form,
                                       error=error, title="Регистрация",
                                       current_users=None,
                                       message=None)
                
        elif not form.validate_on_submit():
            return render_template("users/register.html", form=form,
                                   title="Регистрация",
                                   current_users=None,
                                   message=None
                                   )
        
        return render_template("users/register.html", form=form,
                               title="Регистрация",
                               current_users=None,
                               message=None)
        # response = render_template(render_template("users/register.html"))
        # return render_template("users/register.html", form=form)

    @app_.route(
        "/login",
        methods=[
            "GET",
            "POST"
        ],
    )
    async def login():
        # Логика аутентификации пользователя
        form_loginin = GetFormAuthorization()  # Создаем экземпляр формы
        sess = Session()
        
        user = None
        if form_loginin.validate_on_submit():
            email = form_loginin.email.data
            password = form_loginin.password.data
            user = sess.query(Users).filter_by(email=email).first()
        if request.method == "POST":
        
            
                # Received user
                
                user.set_password(password)
                """
                    На каком этапе лучше создавать хеш-пароль???
                    Хешировать email или нет???
                """
                
                # Compare the email and password
                """
                    Сравнение проводить лучше в состоянии хеша или
                    декодировать пароль, затем сравнивать???
                """
                if (user.email != email) and\
                  (password != Users.check_password(user.password)):
                    return render_template(
                        "users/login.html",
                        title="Авторизация",
                        current_users=None,
                        form=form_loginin,
                        message="Invalid username or password")
                return render_template(
                    "users/login.html",
                    title="Авторизация",
                    current_users=None,
                    form=form_loginin,
                    message="login successful!"
                    )
        
        if request.args.get('token') != None and\
          len(request.args.get('token')) > 10 :
            login_user(user)
        return render_template("users/login.html",
                               title="Авторизация",
                               current_users=current_user,
                               form=form_loginin,
                               message=None,)

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
                token, salt='email-confirm', max_age=120
                )  # Пример декодирования
            user = sess.query(Users).filter_by(email=email).first()

            # Логика активации пользователя
            if user and user.activation_token == token:
                if user.token_created_at and (
                  datetime.utcnow() - user.token_created_at) < timedelta(
                  minutes=int(TOKEN_TIME_MINUTE_EXPIRE)
                  ):
                    
                    # Удаляем токен после активации
                    user.activation_token = None
                    # Удаляем время создания токена
                    user.token_created_at = None
                    # Активируем пользователя
                    user.is_activated = True
                    flash(
                        'Your account has been activated! You can now log in.',
                        'success'
                        )
                   
                else:
                    flash('Invalid activation token.', 'danger')
                    # Переадресация на страницу входа
                    return redirect(
                        url_for('login')
                        )
            else:
                # Переадресация на страницу входа. Токен не найден.
                flash('Token not found', 'danger')
                return redirect(
                    url_for('login')
                )
            # Переадресация после успешной активации
            return redirect(
                url_for('login')
                )
    
        except Exception as e:
            print(f"[activate]: Error => {e.__str__()}")
            flash('The activation link is invalid or has expired.', 'danger')
            return redirect(
                url_for('login', token=token)
                )  # Переадресация на страницу входа
        finally:
            sess.commit()
            sess.close()
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
    @login_manager.user_loader
    def load_user(user_id):
        # Логика загрузки пользователя из базы данных по user_id
        return Users.get(user_id)
        
    return app_

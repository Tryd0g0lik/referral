"""Here a router of the flask app."""

from datetime import datetime, timedelta
from flask import render_template, request
# from referral.flasker import csrf
from flask import session as s
import asyncio as asy
from dotenv_ import TOKEN_TIME_MINUTE_EXPIRE
from referral.flasker import app_, login_manager
from .interfaces.files import receive_js_file

from .models import Session, Users

# from .models_more.model_users import Users

from .views_more.views_account import views_accouts
from .views_more.views_profile import views_profiles
from .views_more.views_referral import views_referrals


async def app_router() -> str:
    """Total function"""
    await asy.gather(
    asy.create_task(views_accouts(app_)),
    asy.create_task(views_profiles(app_)),
    asy.create_task(views_referrals(app_)),
    )
    
    def delete_old_users():
        """Here  all tokens we delete where token time was expired session['_user_id']"""
        sess = Session()
        try:
            threshold_time = datetime.utcnow() - timedelta(
                minutes=int(TOKEN_TIME_MINUTE_EXPIRE)
            )
            old_users = (
                sess.query(Users).filter(Users.token_created_at < threshold_time).all()
            )
            
            # DEVelop's mode - The status "is_active" (from db) - cleaning
            s['_user_id'] = None
            if len(old_users) > 0:
                for user in old_users:
                    # sess.delete(user)
                    u = sess.query(Users).filter_by(id=user.id).first()
                    u.activation_token = None
                    
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
    async def main_page() -> str:
        """
        Here is a main page uploading
        :return:
        """
        # Below, receive the JS file name.
        js_file_name = receive_js_file()
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
            # Below, receive the JS file name.
            js_file_name = receive_js_file()
        return render_template("index.html",
                               message=None,
                               js_file_name=js_file_name)

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
    from .models import Session
    from .models_more.model_users import Users
    from referral.interfaces.user_login import UserLogin

    sess = Session()
    user = sess.query(Users).filter_by(id=int(user_id)).first()
    userlogin = UserLogin()
    userlogin.create(user)
    user_id = userlogin.get_id()
    
    userlogin.fromDB(user_id)
    sess.close()

    return userlogin

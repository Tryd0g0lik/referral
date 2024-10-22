from datetime import datetime, timedelta

from cfgv import ValidationError
from flask import (flash, redirect, render_template, request,  # jsonify,
                   url_for)
from flask_login import login_user, login_required
from itsdangerous import URLSafeTimedSerializer
# URL-TOKEN

from referral.flasker import csrf
from referral.forms.form_referral import GetFormReferralCode
from referral.user_login import UserLogin
from dotenv_ import TOKEN_TIME_MINUTE_EXPIRE
from referral.forms.form_registration import GetFormRegistration
from referral.forms.form_login import GetFormAuthorization
from referral.models import Session
from referral.models_more.model_users import Users
from referral.postman.sender import send_activation_email



def views_referrals(app_):
    # https://itsdangerous.palletsprojects.com/en/2.2.x/url_safe/#itsdangerous.url_safe.URLSafeSerializer
    s = URLSafeTimedSerializer(
        secret_key=app_.secret_key,
        
    )
    @app_.route(
        "/profile/referral",
        methods=[
            "GET",
        ]
    )
    @login_required
    async def referral_form():
        """This present a list of referral-code"""
        message = "OK"
        form_referral = GetFormReferralCode()
        if request.method == "GET":
            pass
       
        return render_template(
            "users/referral_code.html",
            title="Создать referral code",
            form=form_referral,
            message=message,
        )

    @app_.route(
        "/profile/referral/delete",
        methods=[
            "GET", "POST"
        ]
    )
    @login_required
    async def referral_delete():
        """This present a list of referral-code"""
        pass

    @app_.route(
        "/profile/referral/add",
        methods=[
            "POST"
        ]
    )
    @login_required
    async def referral_add():
        """This present a list of referral-code"""
        message = "OK"
        form_referral = GetFormReferralCode()
        if request.method == "POST" and form_referral.validate_on_submit():
            pass
        
        return render_template(
            "users/referral_code.html",
            title="Создать referral code",
            form=form_referral,
            message=message,
        )
    
    @app_.route(
        "/profile/referral/change",
        methods=["POST", "GET"]
    )
    @login_required
    async def referral_change():
        pass
        
    return app_
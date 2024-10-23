from flask import (render_template, request)
from flask_login import  login_required
from referral.forms.form_referral import GetFormReferralCode



async def views_referrals(app_):
    
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
        form = GetFormReferralCode()
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            description = form.email.data
            """"
            
            Проверить наличие почты в базе .
            После создать ссылку
            хешировать.
            
            
            """
        
        return render_template(
            "users/referral_code.html",
            title="Создать referral code",
            form=form,
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
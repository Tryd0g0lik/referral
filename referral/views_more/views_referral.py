"""This is a postman for the flask's route.
This a route has logic for work with the referral code
"""

from flask import redirect, render_template, request, url_for, jsonify
from flask_login import login_required

from referral.forms.form_referral import GetFormReferralCode
from referral.interfaces.files import receive_pathname_js_file
from referral.interfaces.referral_code_remove import sub_defReferralCodeRemove
from referral.models import Session


async def views_referrals(app_):
    """
    This is a postman for the flask's route.
    This a route has logic for work with the referral code
    """

    @app_.route(
        "/profile/referral",
        methods=[
            "GET",
        ],
    )
    @login_required
    async def referral_form():
        """This present a list of referral-code"""
        message = "OK"
        form_referral = GetFormReferralCode()
        
        # Below, receive the JS file name.
        js_file_name = receive_pathname_js_file()
        if request.method == "GET":
            pass

        return render_template(
            "users/referral_code.html",
            title="Создать referral code",
            form=form_referral,
            message=message,
            js_file_name=js_file_name,
        )

    @app_.route("/profile/delete", methods=["GET"])
    @login_required
    async def referral_delete():
        """This present a list of referral-code"""
        js_file_name = receive_pathname_js_file()
        
        return render_template(
            "users/profile_delete.html",
            title="Удалить профиль",
            form=None,
            message=None,
            js_file_name=js_file_name,
        )
        
    @app_.route("/profile/referral/add", methods=["POST"])
    @login_required
    async def referral_add():
        return redirect(url_for("profiles"))


    return app_

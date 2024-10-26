"""Views of profile"""
import os

from flask import (render_template, session, request)
from flask_login import login_required
from referral.forms.form_login import GetFormAuthorization
# LOCAL LIB
from referral.flasker import app_type
from referral.interfaces.files import receive_js_file
from referral.models import Session
from referral.models_more.model_referral import Referrals


async def views_profiles(app_) -> app_type:
    """
    Parent for account's interface.
    :param app_: This is a flask's app
    :return: app_
    """
    # PROFILE
    @app_.route(
        "referral_form",
        methods=[
            "GET",
        ],
    )
    @login_required
    async def profiles() -> str:
        """Opening a page for the user authorized
        This present a list of referral-code"""
        
        message = [m.args['message'] if len(m.args) > 0 and m.args['message']
                   else "Profile" for m in [request]][0]
        
        GetFormAuthorization()
        sess = Session()
        # Below, receive the JS file name.
        js_file_name = receive_js_file()
        referral_obj_list = sess.query(Referrals).filter(id != 0).all()
        referral_list = []
        if len(referral_obj_list) > 0:
            referral_list = [r.__dict__ for r in referral_obj_list]
            web_host = request.host_url
            
            return render_template(
                "usersreferral_form.html", title="Dashboard", message=message,
                contain=referral_list,
                web_host=web_host,
                js_file_name= js_file_name
            )
        return render_template(
            "users/profile.html",
            title="Dashboard",
            message=message,
            js_file_name=js_file_name
        )

    async def exit():
        # clear session
        # @app_.before_request
        pass
            
    return app_

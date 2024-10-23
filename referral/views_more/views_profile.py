"""Views of profile"""
from flask import (render_template, session)
from flask_login import login_required
from referral.forms.form_login import GetFormAuthorization
# LOCAL LIB
from referral.flasker import app_type

async def views_profiles(app_) -> app_type:
    """
    Parent for account's interface.
    :param app_: This is a flask's app
    :return: app_
    """
    # PROFILE
    @app_.route(
        "/profile",
        methods=[
            "GET",
        ],
    )
    @login_required
    async def profiles() -> str:
        """Opening a page for the user authorized
        This present a list of referral-code"""
        message = "Profile"
        GetFormAuthorization()
    
        return render_template(
            "users/profile.html", title="Dashboard", message=message
        )
    async def exit():
        # clear session
        # @app_.before_request
        pass
            
    return app_

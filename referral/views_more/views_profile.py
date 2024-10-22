"""Views of profile"""
from flask import (render_template)
from flask_login import login_required
from referral.forms.form_login import GetFormAuthorization


def views_profiles(app_):
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
    async def profiles():
        """Opening a page for the user authorized
        This present a list of referral-code"""
        message = "Profile"
        GetFormAuthorization()
    
        return render_template(
            "users/profile.html", title="Dashboard", message=message
        )
    return app_

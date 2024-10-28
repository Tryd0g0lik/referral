"""This is a postman for the flask's route.
This a route has logic for work with the referral code
"""

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from referral.forms.form_referral import GetFormReferralCode
from referral.interfaces.files import receive_pathname_js_file
from referral.models import Session
from referral.models_more.model_referral import Referrals
from referral.models_more.model_users import Users


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

    @app_.route("/profile/referral/delete", methods=["GET", "POST"])
    @login_required
    async def referral_delete():
        """This present a list of referral-code"""
        pass

    @app_.route("/profile/referral/add", methods=["POST"])
    @login_required
    async def referral_add():
        return redirect(url_for("profiles"))
#         """This present a list of referral-code
#         При авторизации надо в куки разместить ключ пользователя.
#         """
        # Below, receive the JS file name.
        # js_file_name = receive_pathname_js_file()
        # message = "OK"
        # form = GetFormReferralCode()
#         if request.method == "POST" and form.validate_on_submit():
#             """Descript receive for referrals code """
#             # strBool = form.validator_register_email(form.email)
#             # if type(strBool) == bool:
#             #     message="Your email address did not go checking!"
#             #     response = jsonify(
#             #         message=message,
#             #     )
#             #     return response
#             #
#             # email = strBool[0:]
#
#             description = [
#                 d.data if d and len(d.data) > 0 else "" for d in [form.description]
#             ]
#
#             sess = Session()
#             try:
#                 email = ""
#                 u = sess.query(Users).filter_by(email=email).first()
#                 if u.email == email:
#                     message = "Данный email уже был"
#                     return redirect(url_for("profiles", message=message))
#                 ref = Referrals(u)
#                 ref.description = description[0]
#                 ref.is_send = True
#                 sess.add(ref)
#                 sess.commit()
#             except Exception as e:
#                 print(
#                     f"""[referral_add]: Something what wrong!
# Error => {e}"""
#                 )
#
#             finally:
#                 sess.close()
#
#             """"
#             generate_unique_referral_code
#             Проверить наличие почты в базе .
#             После создать ссылку
#             хешировать.
#             """
#
#         return render_template(
#             "users/referral_code.html",
#             title="Создать referral code",
#             form=form,
#             message=message,
#             js_file_name=js_file_name,
#         )

    @app_.route("/profile/referral/change", methods=["POST", "GET"])
    @login_required
    async def referral_change():
        pass

    return app_

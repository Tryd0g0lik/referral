from flask import (render_template, request, jsonify, redirect, url_for)
from flask_login import  login_required
from referral.forms.form_referral import GetFormReferralCode
# from referral.interfaces.tokenization import EmailToGenerateToken
from referral.models import Session, Users, Referrals




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
        """This present a list of referral-code
        При авторизации надо в куки разместить ключ пользователя.
        """

        message = "OK"
        form = GetFormReferralCode()
        if request.method == "POST" and form.validate_on_submit():
            # strBool = form.validator_register_email(form.email)
            # if type(strBool) == bool:
            #     message="Your email address did not go checking!"
            #     response = jsonify(
            #         message=message,
            #     )
            #     return response
            #
            # email = strBool[0:]
            description = [d.data if d and len(d.data) > 0 else ''
                           for d in [form.description] ]
            
            sess = Session()
            try:
                # r = EmailToGenerateToken(app_)
                # referral_token = r.generate_dumps_token(email)
                u = sess.query(Users).filter_by(email = email ).first()
                if u.email == email:
                    message = "Данный email уже был"
                    return redirect(url_for("profiles", message=message))
                ref = Referrals(u)
                ref.description = description[0]
                ref.is_send = True
                sess.add(ref)
                sess.commit()
            except Exception as e:
                print(f"""[referral_add]: Something what wrong!
Error => {e}""")
            
            finally:
                sess.close()
            
            
            """"
            generate_unique_referral_code
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
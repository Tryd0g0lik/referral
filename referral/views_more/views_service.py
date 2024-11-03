"""
For a work with API-request.
"""

from flask import (jsonify, request, redirect, url_for)
from flask_login import login_required
from flask_wtf.csrf import generate_csrf

from referral.flasker import app_type
from referral.interfaces.referral_code_remove import sub_defReferralCodeRemove
from referral.models import Session
from referral.models_more.model_referral import Referrals
from referral.models_more.model_users import Users


async def views_services(app_) -> app_type:
    """This is a postman for the flask's rote"""
    
    @app_.route("/api/v1/token/get", methods=["OPTIONS", "POST"])
    @login_required
    async def get_token():
        """
         This is API "/api/v1/token/get" method "POST".
         This API return the user's token ('activation_token') from
          db (Users).
          But, first, us up need the 'user_id' will be receive.
          Then knowing 'user_id' , receive 'activation_token'.
        :return: JSON response which
        has a '{"user_token": < user_token >}'
        or '{"message": "Not OK. Something what wrong "}'
        """
        from referral.interfaces.corser import _build_cors_preflight_response
        
        if request.method == "OPTIONS":
            return _build_cors_preflight_response()
        
        if request.method == "POST":
            """Down, a 'activation_token' (data from db) we sending."""
            data = request.get_json()
            user_id = data.get("userId")
            print("[user_id]: " + user_id)
            sess = Session()
            # Receive data
            if not user_id:
                return jsonify(
                    {"message": "Not OK. Something what wrong "}
                ), 400
            try:
                user = sess.query(Users).filter_by(id=int(user_id)).first()
                if not user:
                    return jsonify(
                        {"message": "Not OK. This 'user_id' invalid."}
                    ), 400
                user_token = user.activation_token
                sess.close()
                
                # "OPTIONS"
                if request.method == "OPTIONS":
                    # CORS
                    return _build_cors_preflight_response()
                
                resp = {"user_token": user_token}
                data_json = jsonify(resp), 201
                
                return data_json
            except Exception as e:
                print(f"[get_token]: Something what wrong! Error = > {e}")
                return jsonify({"message": "Not OK. Error!"}), 400
        else:
            print("[get_token]: Not Ok")
            return jsonify({"message": "Not OK."}), 400
    
    @app_.route("/api/v1/referral/add", methods=["OPTIONS", "POST"])
    @login_required
    async def add_referral_code():
        """
        This is API "/api/v1/referral/add" method "POST".
        
        Entry point receiving JSON-string '
        {
          "userToken": < your_token >,
          "descript": < your_description > or "{Make}"
        }'.
        
        This API return the user's token ('activation_token' look above) from
         db (Referrals). But, first, us up need
          the 'user_id' get and make check.
        :param: 'user_token': string. Through 'user_token' we get the 'user_id'.
        By 'user_id' , checking the presence 'referral_code' in db.
        If a  object is result verification 'referral_code' (from
        the table db "referrals"), return  a JSON-string
        '{"message": "На email ссылка уже опубликована",
                         "descript": None,
                         "referral": None,
                         }' asn status code 200.
        or add the new line.
        :param: 'description': string. By a default value -
          '{Make}' or text of user.
        
        :return: Receive a new token's code if all Ok.
        '{'message': "OK", "descript": < your_description >,
            'referral': < your_referral_code> }' and
        status 200.
        If not all OK, receiving
        '{"message": "Not Ok",
         "descript": None,
          "referral": None, }' and
        status 400.
        """
        from referral.interfaces.corser import _build_cors_preflight_response
        sess = Session()
        response = jsonify({"message": "Not Ok",
                            "descript": None,
                            "referral": None,
                            }), 400
        try:
            if request.method == "OPTIONS":
                return _build_cors_preflight_response()
            
            if request.method == "POST":
                """Descript receive for referrals code """
                data = request.get_json()
                descript = data.get('descript')
                user_token = data.get('userToken')
                # Is search the user
                user = sess.query(Users)\
                    .filter_by(activation_token=user_token).first()
                
                if not user:
                    return response
                response = \
                    jsonify(
                        {"message": "На email ссылка уже опубликована",
                         "descript": None,
                         "referral": None,
                         }
                    ), 200
                user_index = user.id
                sess.close()
                referral_user = sess.query(Referrals)\
                    .filter_by(user_id=user_index).all()
                
                if len(list(referral_user)) == 0:
                    # Is calculating a referral's code from user
                    # reff = Referrals(user.email)
                    referral_code_obj = Referrals(user)
                    referral_code_obj.description = \
                        [d if len(d) > 0 else 'Null' for d in [descript]]
                    
                    response = jsonify(
                        {"message": "Ok",
                         "descript": referral_code_obj.description,
                         "referral": referral_code_obj.referral_code}), 200

                    sess.add(referral_code_obj)
                    sess.commit()
        except Exception as e:
            print(
                f"""[referral_add]: Something what wrong!
        Error => {e}"""
            )
        
        finally:
            sess.close()
            return response

    @app_.route("/api/v1/referral/get", methods=["OPTIONS", "POST"])
    @login_required
    async def get_referral_code():
        """
        This is API "/api/v1/referral/get" method "POST"
        
         Entry point receiving JSON-string '
        {
          "userToken": < your_token >,
        }'.
        
        This API return the user's token ('activation_token' look above) from
         db (Referrals). But, first, us up need
          the 'user_id' get and make check.
        :param: 'user_token': string. Through 'user_token' we get the 'user_id'.
        By 'user_id' , checking the presence 'referral_code' in db.
        If a object is result of verification 'referral_code' (from
        the table db "referrals"),
         :return: a JSON-string
        '{"message": "Нв email ссылка уже опубликована",
                         "descript": < description > ,
                         "referral": < referral_code >,
                         }' and status code 200.
        or  '{'message': "Пользователь не имеет referral-кода.",
                     "descript": None,
                     "referral": None,}' and status code 200.
        If not all OK
        '{"message": "Not Ok",
          "descript": None,
          'referral': None }' and
        status code 400.
        
        """
        from referral.interfaces.corser import _build_cors_preflight_response
        sess = Session()
        response = jsonify({"message": "Not Ok", 
                            "descript": None, 
                            "referral": None,}), 400
        try:
            if request.method == "OPTIONS":
                return _build_cors_preflight_response()

            data = request.get_json()
            user_token = data.get('userToken')
            
            # Is search the user
            user = sess.query(Users) \
                .filter_by(activation_token=user_token).first()
            
            if not user:
                return response
            response = \
                jsonify(
                    {"message": "Пользователь не найден.", 
                     "descript": None,
                     "referral": None}
                ), 200
            sess.close()
            user_referral = sess.query(Referrals).filter_by(user_id=user.id)\
                .first()
            if not user_referral:
                response = jsonify(
                    {'message': "Пользователь не имеет referral-кода.",
                     "descript": None,
                     "referral": None,}
                ), 200
                
            response = jsonify(
                {'message': "OK", 
                 "descript": user_referral.description,
                 "referral": user_referral.referral_code}
            ), 200
            
        except Exception as e:
            print(
                f"""[referral_add]: Something what wrong!
        Error => {e}"""
            )

        finally:
            sess.close()
            return response

    @app_.route('/<regex("[\w\d]{5,}"):referral_code>', methods=["GET"])
    async def get_authorization_referral_code(referral_code: str):
        sess = Session()
        response = \
            jsonify(
                {"message": "ссылка не найдена",
                 "descript": None,
                 "referral": None}
            ), 404
        try:
            reff = sess.query(Referrals).filter_by(referral_code=referral_code)\
                .first()
            if not reff:
                return response
            if reff.is_activated:
                return jsonify(
                    {"message": "Ссылка устарела.",
                     "descript": None,
                     "referral": None}
                ), 200
            reff.is_activated = True
            sess.add(reff)
            sess.commit()
            return redirect(url_for("login",
                                    message="Ok",
                                    descript="Первые введенные данные зайт \
запомнит как регистрация аккаунта.",
                                    token=referral_code))
        except Exception as e:
            print(f"[get_authorization_referral_code]: Error => {e.__str__()}")
            return redirect(url_for("login"))
        finally:
            sess.commit()
            sess.close()
            
    @app_.route("/api/v1/remove", methods=["POST", "OPTIONS"])
    async def remove_profile():
        sess = Session()
        response: object = {}
        try:
            # Delete a referral code
            result = sub_defReferralCodeRemove(sess)
            index = result["index"]
            response = result["response"]
            # re-search
            user = sess.query(Users).filter_by(id=index) \
                .first()
            # Delete the record
            sess.delete(user)
            # #Commit change to the database
            sess.commit()
            sess.close()
            return redirect(url_for("main_page"))
        except Exception as e:
            print(
                f"""[remove_profile]: Something what wrong!
            Error => {e}"""
            )
            return response
        finally:
            sess.close()

    @app_.route("/api/v1/profile/referral/delete", methods=["POST", "OPTIONS"])
    @login_required
    async def referral_delete() -> object:
        """
        Removing referral code od user
        :return: object from jsonify
        """
        sess = Session()
        response: object = {}
        try:
            # Delete a referral code
            result = sub_defReferralCodeRemove(sess)
            index = result["index"]
            response = result["response"]
        
            sess.close()
            return response
        except Exception as e:
            print(
                f"""[remove_profile]: Something what wrong!
                    Error => {e}"""
            )
            return response
        finally:
            sess.close()

    @app_.route("/csrf_token", methods=["GET"])
    def get_csrf_token():
        """
        This CSRF-key returning by 'GET' request/
        :return: JSON '{"csrf_token": < csrf_key >}'
        """
        csrf_ = generate_csrf()

        return jsonify({"csrf_token": csrf_}), 200

    return app_

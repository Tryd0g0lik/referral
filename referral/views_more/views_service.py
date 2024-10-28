"""
For a work with API-request.
"""

from flask import jsonify, request
from flask_login import login_required
from flask_wtf.csrf import generate_csrf

from referral.flasker import app_type
from referral.models import Session
from referral.models_more.model_referral import Referrals
from referral.models_more.model_users import Users


async def views_services(app_) -> app_type:
    """This is a postman for the flask's rote"""
    
    @app_.route("/api/v1/token/get", methods=["OPTIONS", "POST"])
    @login_required
    async def get_token():
        """
        This a function return user's 'activation_token' from db.
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
    async def get_referral_code():
        from referral.interfaces.corser import _build_cors_preflight_response
        sess = Session()
        response = jsonify({"message": "Not Ok"}), 400
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
                        {"message": "Нв email ссылка уже опубликована"}
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
    

    
    @app_.route("/csrf_token", methods=["GET"])
    def get_csrf_token():
        """
        This CSRF-key returning by 'GET' request/
        :return: JSON '{"csrf_token": < csrf_key >}'
        """
        csrf_ = generate_csrf()

        return jsonify({"csrf_token": csrf_}), 200

    return app_

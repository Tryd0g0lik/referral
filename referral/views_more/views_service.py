"""
For a work with API-request.
"""

from flask import jsonify, request
from flask_login import login_required
from flask_wtf.csrf import generate_csrf

from referral.flasker import app_type
from referral.models import Session
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

    @app_.route("/csrf_token", methods=["GET"])
    def get_csrf_token():
        """
        This CSRF-key returning by 'GET' request/
        :return: JSON '{"csrf_token": < csrf_key >}'
        """
        csrf_ = generate_csrf()

        return jsonify({"csrf_token": csrf_}), 200

    return app_

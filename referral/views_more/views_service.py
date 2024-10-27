from flask import (render_template, request, jsonify, redirect, url_for)
from flask_login import login_required
from referral.flasker import app_type
from referral.interfaces.corser import _corsify_actual_response, \
    _build_cors_preflight_response
from referral.models import Session, Users, Referrals
from flask_cors import cross_origin
async def views_services(app_) -> app_type:
    
    @app_.route(
        '/api/v1/token/get',
        methods=["GET", "OPTIONS", "POST"]
    ) # /<string:user_id>
    @cross_origin
    async def get_token(user_id):
        print(user_id)
        sess = Session()
        if not user_id :
            return jsonify({"message": "Not OK. Something what wrong "}), 400
        user = sess.qquery(Users).filter_by(id=int(user_id)).first()
        if len(user) == 0:
            return jsonify({"message": "Not OK. This 'user_id' invalid."}), 400
        user_token = user[0].activation_token
    
        if request.method == "OPTIONS":  # CORS preflight
            return _build_cors_preflight_response()
        elif request.method == "POST":
            response = jsonify({"user_token": user_token, "message": "Ok"}), 200
            return _corsify_actual_response(response)
        else:
            return jsonify({"message": "Not OK."}), 400
    return app_
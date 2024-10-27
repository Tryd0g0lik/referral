import json

from flask import (render_template, request, jsonify, redirect, url_for,
                   Response, make_response)
from flask_login import login_required
from flask_wtf.csrf import generate_csrf

from referral.flasker import app_type
from referral.interfaces.corser import _corsify_actual_response, \
    _build_cors_preflight_response
from flask_wtf import csrf
from referral.models import Session, Users, Referrals
from flask_cors import cross_origin
async def views_services(app_) -> app_type:
    
    @app_.route(
        '/api/v1/token/get',
        methods=["OPTIONS", "POST"]
    ) # /<string:user_id>
    @login_required
    async def get_token():
        
        
        if request.method == "OPTIONS":
            
            return _build_cors_preflight_response()

        if request.method == "POST":
            data = request.get_json()
            user_id = data.get('userId')
            print("[user_id]: " + user_id)
            sess = Session()
            if not user_id :
                return jsonify({"message": "Not OK. Something what wrong "}), 400
            user = sess.query(Users).filter_by(id=int(user_id)).first()
            if not user:
                return jsonify({"message": "Not OK. This 'user_id' invalid."}), 400
            user_token = user.activation_token

            if request.method == "OPTIONS":  # CORS preflight
                return _build_cors_preflight_response()
            elif request.method == "POST":
                resp = {"user_token": user_token}
                data_json = \
                    jsonify(
                        resp
                    ), 201
                
                # response = Response(
                #     response=json.dumps({"user_token": user_token}),
                #     status=200,
                #     mimetype='application/json'
                # )
                return data_json # _corsify_actual_response(response)
                # return {
                #     "data": resp,
                #     "status": 203
                # }
            else:
                return jsonify({"message": "Not OK."}), 400
        return jsonify({"message": "Not OK."}), 400
    
    @app_.route(
        "/csrf_token",
        methods=["GET"]
    )
    def get_csrf_token():
        csrf_ = generate_csrf()
        
        return jsonify({"csrf_token": csrf_}), 200
    return app_


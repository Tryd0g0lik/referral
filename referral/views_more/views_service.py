from flask import (render_template, request, jsonify, redirect, url_for)
from flask_login import login_required
from referral.flasker import app_type


async def views_services(app_) -> app_type:
    
    @app_.route(
        '/api/v1/token/get',
        methods=["POST", "OPTIONS"]
    )
    @login_required
    async def get_token():
        response = app_.make_response()
        response.headers[
            'Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers[
            'Access-Control-Allow-Headers'] = 'Content-Type, X-CSRFToken'
        print('TEST')
        """"
        status=200,
                       mimetype='application/json'
        """
        
        return jsonify({"user_token": "TEST"})
    return app_
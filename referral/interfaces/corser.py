<<<<<<< HEAD
"""CORS for working with the requests 'POST'. 'OPTION' """
from flask import make_response


def _corsify_actual_response(response):
    """Here,  working POST. Not used now"""
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response


def _build_cors_preflight_response():
    """Here,  working POST"""
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Access-Control-Allow-Credentials", True)

    return response
=======
from flask import make_response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
>>>>>>> f2f5cb55577ec9e548977089419274b159a71883

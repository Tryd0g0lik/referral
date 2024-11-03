"""
The 'sub_defReferralCodeRemove' saving in this file.
"""
import json

from flask import (jsonify, request)
from typing import TypedDict
from referral.models_more.model_referral import Referrals
from referral.models_more.model_users import Users

class TypeReferralRemove(TypedDict):
    """
    This determins data-type which this a function 'sub_defReferralCodeRemove'
    will return.
    """
    index: int
    response: object
def sub_defReferralCodeRemove(sess) -> TypeReferralRemove:
    """
    This a sub-function work in 'remove_profile' and 'referral_delete'.
    :param sess: session(). Removing a referral code from the db;
    :return: {"index": int, "response": JSON_from_jsonify }
    """
    from referral.interfaces.corser import _build_cors_preflight_response
    
    response = \
        jsonify(
            {"message": "профиль не найден",
             "descript": None,
             "referral": None}
        ), 404
    
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    
    data = request.get_json();
    user_token = data.get("userToken")
    
    # Is search the user
    user = sess.query(Users) \
        .filter_by(activation_token=user_token).first()
    
    if not user:
        return response
    response = \
        jsonify(
            {"message": "Пользователь удален.",
             "descript": None,
             "referral": None}
        ), 200
    index = user.id
    sess.close()
    user_referral = sess.query(Referrals).filter_by(user_id=index) \
        .first()
    if not user_referral:
        response = jsonify(
            {'message': "Пользователь не нaйден.",
             "descript": None,
             "referral": None, }
        ), 200
    else:
        # Delete referral code the record
        sess.delete(user_referral)
        sess.commit()
    sess.close()
    
    return {"index": index, "response": response}

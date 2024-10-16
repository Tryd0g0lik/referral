from flask import jsonify
from flasker import app
from flask_jwt_extended import create_access_token, jwt_required

def app_router():
    @app.route('/register', methods=['POST',])
    def register():
        # Логика регистрации пользователя
        pass
    
    @app.route('/login', method=['POST',])
    def login(requests):
        # Логика аутентификации пользователя
        username = requests.json.get('username')
        password = requests.json.get('password')
        # Проверка пользователя и создание токена
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    @app.route('/referal_code', methods=['POST'])
    @jwt_required()
    def create_referral_code():
        # Логика создания реферального кода
        pass
        
    @app.route('/referrals/<referrer_id>', method=['GET'])
    @jwt_required()
    def get_referrals(referral_id):
        # Логика получения рефералов
        pass
    return app
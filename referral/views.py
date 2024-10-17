"""Here a router of the flask app."""

from flask import render_template, request  # jsonify,

# from flask_jwt_extended import create_access_token, jwt_required


def app_router(app_):
    """Total function"""
    @app_.route(
        "/",
        methods=[
            "GET",
            "POST",
        ],
    )
    def upload_main_page():
        """
        Here is a main page uploading
        :return:
        """
        if request.method == "GET":
            pass
        elif request.method == "POST":
            # Предположим, что вы получаете данные из формы
            # Преобразование данных формы в словарь
            # params = request.form.to_dist()
            pass
        return render_template(
            "index.html",
        )

    @app_.route(
        "/register",
        methods=[
            "GET",
        ],
    )
    async def register():
        # Логика регистрации пользователя

        # response = render_template(render_template("users/register.html"))
        return render_template("users/register.html")

    # @app_.route(
    #     "/login",
    #     methods=[
    #         "POST",
    #     ],
    # )
    # async def login():
    #     # Логика аутентификации пользователя
    #     username = await request.json.get("username")
    #     password = await request.json.get("password")
    #     # Проверка пользователя и создание токена
    #     access_token = create_access_token(identity=username)
    #     return jsonify(access_token=access_token)

    # @app_.route(
    #     "/registrator",
    #     methods=[
    #         "POST",
    #     ],
    # )
    # async def login():
    # Логика аутентификации пользователя
    # username = await request.json.get("username")
    # email = await request.json.get("email")
    # Проверка пользователя и создание токена
    # access_token = create_access_token(identity=username)

    # return jsonify(access_token=access_token)

    # @app_.route("/referal_code", methods=["POST"])
    # @jwt_required()
    # async def create_referral_code():
    #     # Логика создания реферального кода
    #     pass
    #
    # @app_.route("/referrals/<referrer_id>", methods=["GET"])
    # @jwt_required()
    # async def get_referrals(referral_id):
    #     # Логика получения рефералов
    #     pass

    return app_

from src.service.user_service import get_user, get_users_all


def init_user(app):
    @app.route("/users", methods=["GET"])
    def route_get_users_all():
        return get_users_all()

    @app.route("/users/<int:id>", methods=["GET"])
    def route_get_users(id: int):
        return get_user(id)

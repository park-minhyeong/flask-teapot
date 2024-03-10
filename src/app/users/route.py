from flask import jsonify, make_response
def init_user(app):
    @app.route("/users", methods=["GET"])
    def user():
        response = make_response(jsonify([{"name": "John Doe", "email": "john@test.com"}]), 200)
        return response  
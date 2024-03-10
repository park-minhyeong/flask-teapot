from flask import make_response
def init_root(app):
    @app.route("/", methods=["GET"])
    def teapot():
        response = make_response("I'm a teapot", 418)
        return response
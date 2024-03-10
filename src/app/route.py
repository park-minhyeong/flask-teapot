def init_root(app):
    @app.route("/")
    def hello_world():
        return "Helloasd, Worsasdasddsdlsafaasdasdsdasfddasdsdasfsdasdf!"

from flask import Flask

def create_app():
    app = Flask(__name__)
    from src.app.route import init_root
    from src.app.users.route import init_user
    
    init_root(app)
    init_user(app)
    

    return app

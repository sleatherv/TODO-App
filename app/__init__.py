from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth
from flask_login import LoginManager
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)


# @login_manager.user_loader
# def load_users(user_id):
#     return


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    login_manager.init_app(app)
    # csrf = CSRFProtect(app)
    app.config.from_object(Config)

    app.register_blueprint(auth)

    return app
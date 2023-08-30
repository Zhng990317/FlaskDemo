#工厂
from flask import Flask

import settings
from blueprints.home import home_bp
from blueprints.user import user_bp


def create_app():

    app = Flask(__name__)
    #加载配置
    app.config.from_object(settings.BaseConfig)
    #注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(home_bp)
    #实例化扩展

    return app

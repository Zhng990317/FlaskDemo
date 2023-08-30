from flask import Blueprint

#构造蓝图
home_bp = Blueprint("home", __name__, template_folder=r'E:\GithubRepositories\flaskDemo\tamplates\home')
#导入使用蓝图的视图对象
from . import home
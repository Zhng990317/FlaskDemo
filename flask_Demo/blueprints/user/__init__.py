from flask import Blueprint

#构造蓝图
user_bp = Blueprint("user", __name__, template_folder=r'E:\GithubRepositories\flaskDemo\tamplates\user')
#导入使用蓝图的视图对象
from . import login
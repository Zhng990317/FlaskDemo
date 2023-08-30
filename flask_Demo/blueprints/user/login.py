from blueprints.user import user_bp
from flask import render_template

@user_bp.route('/login/', methods=["POST", "GET"])
def login():
    return render_template('login.html')
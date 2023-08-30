from blueprints.home import home_bp
from flask import render_template

@home_bp.route('/home/')
def home():
    return render_template('home.html')

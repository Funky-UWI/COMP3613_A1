from flask import Blueprint, redirect, render_template, request, send_from_directory,url_for
from flask_jwt import unauthorized_loader
index_views = Blueprint('index_views', __name__, template_folder='../templates')

# @jwt.unauthorized_loader
# def custom_unauthorized_response(_err):
#     return redirect(url_for('login'))

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('signup.html')

@jwt_required
@index_views.route('/home',methods=['GET'])
def home():
    return render_template("index.html") 

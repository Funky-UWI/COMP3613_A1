from flask import Blueprint, redirect, render_template, request, send_from_directory,url_for
from flask_jwt_extended import jwt_required
index_views = Blueprint('index_views', __name__, template_folder='../templates')

# 
@index_views.route('/', methods=['GET'])
@jwt_required(optional=False)
def index_page():
    return render_template('index.html')


@index_views.route('/signup',methods=['GET'])
def home():
    return render_template("signup.html")

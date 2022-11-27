from flask import Blueprint, redirect, render_template, request, send_from_directory,current_user,url_for

index_views = Blueprint('index_views', __name__, template_folder='../templates')

# @jwt_required
@index_views.route('/', methods=['GET'])
def index_page():
      
    return render_template('signup.html')

@index_views.route('/home',methods=['GET'])
def home():
    if current_user.is_authenticated():
        return render_template("home.html") #Replace with home templateS
    else:
        redirect(url_for('Login'))
from flask import Blueprint, redirect, render_template, request, send_from_directory

index_views = Blueprint('index_views', __name__, template_folder='../templates')

# @jwt_required
@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('signup.html')
from flask import Blueprint, render_template, jsonify, request, send_from_directory, redirect, url_for, flash
from flask_jwt import jwt_required
from App.controllers import *

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.get_json()
        author = authenticate(form["email"], form["password"])
        if user:
            return render_template("index.html")
        else:
            flash("Invalid email or password.")
            return render_template("login.html")
    else:
        return render_template("login.html")

@user_views.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        form = request.get_json()
        author = create_author(form["fname"], form["lname"], form["email"], form["password"])
        if not author:
            flash("Author already exists.")
            return render_template("signup.html")
        else:
            flash("Author account succesfully created.")
            return render_template("index.html")

@user_views.route("/<id>/pubtree", methods=["GET"])
def pubtree(id):
    authors, publications = author_publication_tree(id)
    return render_template("pubtree.html", authors=authors, publications=publications)

@user_views.route("/<id>",methods=["GET"])
def author(id):
    author = get_author_by_id(id)
    return render_template("author.html",author = author.toJSON()) #Change to author template
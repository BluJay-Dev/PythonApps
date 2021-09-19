from flask import Blueprint

views = Blueprint(__name__,"Views")


@views.route("/")
def home():
    return "Home Page"

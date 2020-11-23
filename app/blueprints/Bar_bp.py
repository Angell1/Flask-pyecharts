from flask import Blueprint

Bar = Blueprint("Bar", __name__, url_prefix="/Bar")


@Bar.route('/')
def index():
    return "This is home index page."
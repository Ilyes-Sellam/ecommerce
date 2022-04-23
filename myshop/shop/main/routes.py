from flask import Blueprint, request, render_template
from shop.models import Product


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')
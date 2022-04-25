from flask import Blueprint, request, render_template
from shop.models import Categorie, Product


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    try:
        products = Product.query.all()
        categories = Categorie.query.all()
    except Exception as e:
        return str(e)
    if not products or not categories:
        return False
    return render_template('home.html', products=products, categories=categories)


@main.route("/contact")
def contact():
    categories = Categorie.query.all()
    return render_template('contact.html', title='Contact', categories=categories)
import email
from flask import Blueprint, request, render_template
from flask_login import current_user
from shop.models import Categorie, Product, Customer, Cart


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    try:
        products = Product.query.all()
        categories = Categorie.query.all()
        cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
        if cart == None:
            cart_items = 0
        else:
            cart_items = (len(cart.products))
    except Exception as e:
        return str(e)
    if not products or not categories:
        return False
    return render_template('home.html', products=products, categories=categories, cart_items=cart_items)


@main.route("/contact")
def contact():
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    if cart == None:
        cart_items = 0
    else:
        cart_items = (len(cart.products))
    categories = Categorie.query.all()
    return render_template('contact.html', title='Contact', categories=categories, cart_items=cart_items)
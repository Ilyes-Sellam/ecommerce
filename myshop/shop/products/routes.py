from flask import Blueprint, request, render_template
from shop.models import Categorie, Product

products = Blueprint('products', __name__)

@products.route("/product/<string:product_name>", methods=["GET"])
def get_product(product_name):

    try:
        categories = Categorie.query.all()
        product = Product.query.filter_by(product_name=str(product_name)).first()
    except Exception as e:
        return str(e)
    if not product or not categories:
        return False
    return render_template('shop/details.html', product=product, categories=categories)
    
@products.route("/products", methods=["GET"])
def get_products():

    try:
        categories = Categorie.query.all()
        products = Product.query.all()
    except Exception as e:
        return str(e)
    if not products or not categories:
        return False
    return render_template('shop/products_list.html', products=products, categories=categories)


@products.route("/categorie/<int:categorie_id>", methods=["GET"])
def categorie_products(categorie_id):

    try:
        categories = Categorie.query.all()
        categorie = Categorie.query.filter_by(id=categorie_id).first()
        
    except Exception as e:
        return str(e)
    if not categorie or not categories:
        return False
    products = categorie.products
    return render_template('shop/categorie_products.html', products=products, categories=categories)
    
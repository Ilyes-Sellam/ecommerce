from flask import Blueprint, request, render_template
from shop.models import Product

products = Blueprint('products', __name__)

@products.route("/product/<string:product_name>", methods=["GET"])
def get_product(product_name):

    try:
        product = Product.query.filter_by(product_name=str(product_name)).first()
    except Exception as e:
        return str(e)
    if not product:
        return False
    return render_template('shop/details.html', product=product)
    
@products.route("/products", methods=["GET"])
def get_products():

    try:
        products = Product.query.all()
    except Exception as e:
        return str(e)
    if not products:
        return False
    return render_template('shop/products_list.html', products=products)
    
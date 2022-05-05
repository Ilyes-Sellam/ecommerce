from flask import Blueprint, request, render_template, flash, url_for, redirect
from shop.models import Categorie, Order, Product, Cart
from flask_login import login_required, current_user
from shop import db

products = Blueprint('products', __name__)

@products.route("/product/<string:product_name>", methods=["GET"])
def get_product(product_name):

    try:
        categories = Categorie.query.all()
        product = Product.query.filter_by(product_name=str(product_name)).first()
        cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
        if cart == None:
            cart_items = 0
        else:
            cart_items = (len(cart.products))
    except Exception as e:
        return str(e)
    if not product or not categories:
        return False
    return render_template('shop/details.html', cart_items=cart_items, product=product, categories=categories)
    
@products.route("/products", methods=["GET"])
def get_products():

    try:
        categories = Categorie.query.all()
        products = Product.query.all()
        cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
        if cart == None:
            cart_items = 0
        else:
            cart_items = (len(cart.products))
    except Exception as e:
        return str(e)
    if not products or not categories:
        return False
    return render_template('shop/products_list.html', cart_items=cart_items, products=products, categories=categories)


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
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    if cart == None:
        cart_items = 0
    else:
        cart_items = (len(cart.products))
    return render_template('shop/categorie_products.html', cart_items=cart_items, products=products, categories=categories)


@products.route("/cart/product/<int:product_id>/add", methods=["GET"])
@login_required
def add_product(product_id):
    product = Product.query.filter_by(id=int(product_id)).first()
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    if cart == None:
        cart = Cart(customer_id = current_user.get_id())
        cart.products.append(product)
        db.session.add(cart)
        db.session.commit()
        flash('Product Added To Cart !', 'success')
        return redirect(url_for('main.home'))
    else:
        for prod in cart.products:
            if product.id == prod.id:
                flash('Product Already Exist in Cart !', 'danger')
                return redirect(url_for('main.home'))
        cart.products.append(product)
        db.session.commit()
        flash('Product added !', 'success')
        return redirect(url_for('main.home'))


@products.route("/cart", methods=["GET"])
@login_required
def cart():
    categories = Categorie.query.all()
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    if cart == None:
        cart_items = 0
    else:
        cart_items = (len(cart.products))
    products = cart.products
    sub_total_price = 0
    for product in products:
        sub_total_price = sub_total_price + product.product_price
    total_price = sub_total_price + 500
    return render_template('shop/cart.html', cart_items=cart_items, products=products, 
            categories=categories, sub_total_price=sub_total_price, total_price=total_price)


@products.route("/cart/product/<int:product_id>/remove", methods=["GET"])
@login_required
def remove_product(product_id):
    product = Product.query.filter_by(id=int(product_id)).first()
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    cart.products.remove(product)
    db.session.commit()
    flash('Product Removed From Cart !', 'success')
    return redirect(url_for('products.cart'))


@products.route("/checkout", methods=["POST"])
@login_required
def checkout():
    categories = Categorie.query.all()
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    order = Order.query.filter_by(customer_id=current_user.get_id()).first()
    if request.method == 'POST':
        if order == None:
            order = Order(customer_id = current_user.get_id())
            products = cart.products
            for product in products: 
                order.products.append(product)
            cart.products.clear()
            products = order.products
            sub_total_price = 0
            for product in products:
                sub_total_price = sub_total_price + product.product_price
            total_price = sub_total_price + 500
            cart_items = (len(cart.products))
            db.session.add(order)
            db.session.commit()
        else:
            products = cart.products
            for product in products: 
                order.products.append(product)
            cart.products.clear()
            products = order.products
            sub_total_price = 0
            for product in products:
                sub_total_price = sub_total_price + product.product_price
            total_price = sub_total_price + 500
            cart_items = (len(cart.products))
            db.session.commit()
        return render_template('shop/checkout.html', cart_items=cart_items, products=products, 
                categories=categories, sub_total_price=sub_total_price, total_price=total_price)

@products.route("/confirm_order", methods=["POST"])
@login_required
def confirm_order():
    order = Order.query.filter_by(customer_id=current_user.get_id()).first()
    if request.method == 'POST':
        # the order did not turn to true (make sure to solve the problem) 
        order.confirmed = True
        flash('Order has been confirmed', 'success')
    return redirect(url_for('main.home'))
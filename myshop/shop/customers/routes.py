
from flask import render_template, url_for, flash, redirect, Blueprint, request
from shop import db, bcrypt
from shop.customers.forms import (RegistrationFrom, LoginFrom, UpdateAccountFrom)
from shop.models import Customer, Categorie, Cart
from flask_login import login_user, current_user, logout_user, login_required
import boto3


customers = Blueprint('customers', __name__)
client = boto3.client('ses')
kms = boto3.client('kms', region_name='us-east-2')


@customers.route("/customer_register", methods=['GET', 'POST'])
def customer_register():
    categories = Categorie.query.all()
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    if cart == None:
        cart_items = 0
    else:
        cart_items = (len(cart.products))
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        customer = Customer(username=form.username.data,
                    email=form.email.data, address=form.address.data, password=hashed_password)
        client.verify_email_address(EmailAddress=customer.email)
        db.session.add(customer)
        db.session.commit()

        flash(f'You should confirm your email address! Befor log in', 'success')
        return redirect(url_for('customers.customer_login'))
    return render_template('customer_register.html', title='Register', form=form, categories=categories, cart_items=cart_items)


@customers.route("/customer_login", methods=['GET', 'POST'])
def customer_login():
    categories = Categorie.query.all()
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    if cart == None:
        cart_items = 0
    else:
        cart_items = (len(cart.products))
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginFrom()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(email=form.email.data).first()
        if customer and bcrypt.check_password_hash(customer.password, form.password.data):
            response = client.get_identity_verification_attributes(
                       Identities=[customer.email]
                                            )
            res = response['VerificationAttributes'][customer.email]['VerificationStatus']
            if res == 'Success':
                login_user(customer, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))
            else:
                flash(f'You should confirm your email address! Befor log in', 'success')
                return redirect(url_for('customers.customer_login'))
        else:
            flash('log in unsuccessful, please check username and password', 'danger')
    return render_template('customer_login.html', title='Login', form=form, categories=categories, cart_items=cart_items)


@customers.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    form = LoginFrom()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(email=form.email.data).first()
        if customer and bcrypt.check_password_hash(customer.password, form.password.data) and customer.is_admin:
            login_user(customer, remember=form.remember.data)
            return redirect(url_for('admin.index'))
        else:
            flash('log in unsuccessful, please check username and password', 'danger')
    return render_template('customer_login.html', title='Login', form=form)

@customers.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@customers.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    categories = Categorie.query.all()
    cart = Cart.query.filter_by(customer_id=current_user.get_id()).first()
    if cart == None:
        cart_items = 0
    else:
        cart_items = (len(cart.products))
    form = UpdateAccountFrom()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('customers.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    return render_template('account.html', title='Account', form=form, categories=categories, cart_items=cart_items)


    
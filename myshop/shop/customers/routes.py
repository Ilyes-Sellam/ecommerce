from flask import render_template, url_for, flash, redirect, Blueprint, request
from shop import db, bcrypt
from shop.customers.forms import (RegistrationFrom, LoginFrom)
from shop.models import Customer
from flask_login import login_user, current_user, logout_user

customers = Blueprint('customers', __name__)

@customers.route("/customer_register", methods=['GET', 'POST'])
def customer_register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        try:
            customer = Customer(username=form.username.data,
                        email=form.email.data, address=form.address.data, password=hashed_password)
            db.session.add(customer)
            db.session.commit()
        except Exception as e:
            return flash(f'internal error server', 'success')

        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('customers.customer_login'))
    return render_template('customer_register.html', title='Register', form=form)


@customers.route("/customer_login", methods=['GET', 'POST'])
def customer_login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginFrom()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(email=form.email.data).first()
        if customer and bcrypt.check_password_hash(customer.password, form.password.data):
            login_user(customer, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('log in unsuccessful, please check username and password', 'danger')
    return render_template('customer_login.html', title='Login', form=form)


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


    
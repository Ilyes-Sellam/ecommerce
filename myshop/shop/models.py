from sqlalchemy import null
from shop import db, login_manager, admin
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView

order_item = db.Table('order_product',
db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)

add_to_cart = db.Table('carts_products',
db.Column('cart_id', db.Integer, db.ForeignKey('cart.id')),
db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)

@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))


class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(100))
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    orders = db.relationship('Order',  backref='customer')
    cart = db.relationship('Cart',  backref='customer')

    def __init__(self, username, email, address, password):
        self.username= username
        self.email = email
        self.address = address
        self.password = password

    def __repr__(self):
        return self.username



class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50))
    product_price = db.Column(db.Float())

    #turn nullable to False
    image_path = db.Column(db.String(20), nullable=True,
                           default='default.jpg')
    product_size = db.Column(db.String(50))
    product_description = db.Column(db.String(200))
    available = db.Column(db.Boolean, default=True)

    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
    
    order = db.relationship('Order', secondary=order_item, backref='products')
    carts = db.relationship('Cart', secondary=add_to_cart, backref='products')

    def __init__(self, product_name, product_price, categorie_id):
        self.product_name= product_name
        self.product_price = product_price
        self.categorie_id = categorie_id


    def __repr__(self):
        return self.product_name



class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categorie_name = db.Column(db.String(50), nullable=False)

    products = db.relationship('Product',  backref='categorie')

    def __init__(self, categorie_name,):
        self.categorie_name = categorie_name

    def __repr__(self):
        return self.categorie_name


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False, unique=True)


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(MyModelView(Customer, db.session))
admin.add_view(MyModelView(Product, db.session))
admin.add_view(MyModelView(Categorie, db.session))
admin.add_view(MyModelView(Cart, db.session))
admin.add_view(MyModelView(Order, db.session))
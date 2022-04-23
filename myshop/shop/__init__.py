
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.config['SECRET_KEY'] = '42a878b2409e8f01a3aae45d16367273'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ilyes:CS502022@localhost:5432/shopdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
migrate = Migrate(app, db)
admin = Admin(app)


from shop.customers.routes import customers 
from shop.products.routes import products 
from shop.main.routes import main 


app.register_blueprint(customers)
app.register_blueprint(products)
app.register_blueprint(main)


from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__, static_url_path='/AgriNet/static')

app.config['SECRET_KEY'] = 'thisisasecretkey246810'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agri_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
Base = automap_base()


# Models
class CustomerAccounts(Base, UserMixin, db.Model):
    __tablename__ = 'CustomerAccounts'

    CustomerAccountId = db.Column(db.Integer, primary_key=True, nullable=False)
    UserName = db.Column(db.String(100), nullable=False, unique=True)
    Password = db.Column(db.String(100), nullable=False)
    CustomerFullName = db.Column(db.String(60), nullable=False)
    Email = db.Column(db.String(100), nullable=True, unique=True)
    PhoneNumber = db.Column(db.String(45), nullable=True)
    AvatarUrl = db.Column(db.String(200), nullable=True)

    def get_id(self):
        return self.CustomerAccountId


class SellerAccounts(Base, UserMixin, db.Model):
    __tablename__ = 'SellerAccounts'

    SellerAccountId = db.Column(db.Integer, primary_key=True, nullable=False)
    UserName = db.Column(db.String(100), nullable=False, unique=True)
    Password = db.Column(db.String(100), nullable=False)
    SellerFullName = db.Column(db.String(60), nullable=False)
    Email = db.Column(db.String(100), nullable=True, unique=True)
    PhoneNumber = db.Column(db.String(45), nullable=True)
    AvatarUrl = db.Column(db.String(200), nullable=True)

    def get_id(self):
        return self.SellerAccountId


Base.prepare(db.engine, reflect=True)

Category = Base.classes.category
OrderDetail = Base.classes.orderdetail
Orders = Base.classes.orders
Products = Base.classes.products


# CustomerAccounts = Base.classes.customeraccounts
# SellerAccounts = Base.classes.selleraccounts
# ShoppingCarts = Base.classes.shoppingcarts
# Categories = db.Table('categories', db.metadata, autoload=True, autoload_with=db.engine)


@login_manager.user_loader
def load_user(UserId):
    if UserId < 100:
        print("customer runned")
        return CustomerAccounts.query.get(int(UserId))
    else:
        print("seller runned")
        return SellerAccounts.query.get(int(UserId))


from AgriNet.customer import routes

from AgriNet.seller import routes

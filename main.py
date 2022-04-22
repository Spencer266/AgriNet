from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import *
from sqlalchemy.orm import Session, sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agri_db.db'

db = SQLAlchemy(app)
Base = automap_base()
engine = create_engine("sqlite:///agri_db.db")



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
# Models
Category = Base.classes.category
# CustomerAccounts = Base.classes.customeraccounts
OrderDetail = Base.classes.orderdetail
Orders = Base.classes.orders
Products = Base.classes.products
# SellerAccounts = Base.classes.selleraccounts
session = Session(engine)

@app.route("/")
def home():
    # newSeller = SellerAccounts(UserName='testnew', Password='pwd', SellerFullName='seller3')
    session.add(SellerAccounts(UserName='testnew', Password='pwd', SellerFullName='seller3'))
    session.commit()
    sellerAccounts = db.session.query(SellerAccounts).all()
    return render_template('test.html', items=sellerAccounts)


@app.route("/detail")
def details():
    return render_template('shop-details.html')


if __name__ == '__main__':
    app.run(debug=True)

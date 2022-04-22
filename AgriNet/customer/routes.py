from AgriNet import app
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

from AgriNet import db, CustomerAccounts, Products
from AgriNet import login_manager
# def role_required(role):
#     def decorator(f):
#         @wraps(f)
#         def wrap(*args, **kwargs):
#             if current_user.name == role:
#                 return f(*args, **kwargs)
#             else:
#                 flash("You need to be an admin to view that page.")
#                 return redirect(url_for('home'))
#         return wrap
#     return decorator


@login_manager.user_loader
def load_user(CustomerAccountId):
    return CustomerAccounts.query.get(int(CustomerAccountId))


@app.route('/')
def home1():
    return redirect(url_for('home'))


@app.route('/customer/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pass')

        cust = db.session.query(CustomerAccounts).filter_by(UserName=username).first()
        if not cust:
            return redirect('login')

        if check_password_hash(password) != cust.Password:

    return render_template('/customer/login.html')


@app.route('/customer/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        cust = db.session.query(CustomerAccounts).filter_by(Email=email).first()
        if cust:
            flash("Email đã đăng ký")
            return redirect(url_for('register'))

        username = request.form.get('username')
        cust = db.session.query(CustomerAccounts).filter_by(UserName=username).first()
        if cust:
            flash("Tên người dùng đã được sử dụng")
            return redirect(url_for('register'))

        new_cust = CustomerAccounts(
            CustomerAccountId=12,
            UserName=username,
            Password=generate_password_hash(request.form.get('pass')),
            CustomerFullName="Default Customer",
            Email=email,
            PhoneNumber=request.form.get('phone'),
            AvatarUrl="https://www.google.com.vn/url?sa=i&url=https%3A%2F%2Fwww.studyphim.vn%2Fmovies%2Fmemoirs-of-a-geisha&psig=AOvVaw0HyWzdsZ9PK7aYfHanf9Az&ust=1650642844077000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCMjxqPzBpfcCFQAAAAAdAAAAABAJ"
        )

        db.session.add(new_cust)
        db.session.commit()

        login_user(new_cust)

        return redirect(url_for("home"))
    return render_template('/customer/registration.html')


@app.route('/customer/home')
def home():
    sample = db.session.query(Products).all()
    return render_template('/customer/index.html', products=sample)


@app.route('/customer/search-result/<search>')
def search(search):
    pass


@app.route('/customer/productview/<product_id>')
def product(product_id):
    product = db.session.query(Products).filter_by(ProductId=product_id).first()
    return render_template('/customer/product-details.html', product=product)


@app.route('/customer/cart')
def cart():
    return render_template('/customer/shopping-cart.html')


@app.route('/customer/checkout')
def checkout():
    return render_template('/customer/checkout.html')

from AgriNet import app
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from AgriNet import db, SellerAccounts, Products
from AgriNet import login_manager


# @login_manager.user_loader
# def load_user(SellerAccountId):
#     return SellerAccounts.query.get(int(SellerAccountId))

from AgriNet import load_user


@app.route('/seller/login', methods=['GET', 'POST'])
def seller_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        seller = db.session.query(SellerAccounts).filter_by(UserName=username).first()
        if not seller:
            return redirect(url_for('seller_login'))
        if not seller.Password == password:
            return redirect(url_for('seller_login'))
        login_user(seller)
        return redirect(url_for('dashboard'))

    return render_template('/seller/login.html')


@app.route('/seller/register', methods=['GET', 'POST'])
def seller_register():
    if request.method == 'POST':
        email = request.form.get('email')
        seller = db.session.query(SellerAccounts).filter_by(Email=email).first()
        if seller:
            flash("Email đã đăng ký")
            return redirect(url_for('register'))

        username = request.form.get('username')
        seller = db.session.query(SellerAccounts).filter_by(UserName=username).first()
        if seller:
            flash("Tên người dùng đã được sử dụng")
            return redirect(url_for('register'))
        new_seller = SellerAccounts(
            UserName=username,
            Password=generate_password_hash(request.form.get('pass')),
            SellerFullName="Default Customer",
            Email=email,
            PhoneNumber=request.form.get('phone'),
            AvatarUrl="https://www.google.com.vn/url?sa=i&url=https%3A%2F%2Fwww.studyphim.vn%2Fmovies%2Fmemoirs-of-a-geisha&psig=AOvVaw0HyWzdsZ9PK7aYfHanf9Az&ust=1650642844077000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCMjxqPzBpfcCFQAAAAAdAAAAABAJ"
        )

        db.session.add(new_seller)
        db.session.commit()

        login_user(new_seller)

        return redirect(url_for("dashboard"))
    return render_template('/seller/registration.html')


@app.route('/seller/home')
def seller_home():
    current_user_id = current_user.UserName

    return render_template('/seller/index.html')


@app.route('/seller/productview/<product_id>')
def seller_product(product_id):
    return render_template('/seller/product-details.html')


@app.route('/seller/dashboard')
def dashboard():
    seller = current_user
    sellerId = seller.SellerAccountId
    products = db.session.query(Products).filter_by(SellerId=sellerId)
    return render_template('/seller/dashboard.html', products=products, user=current_user)


@app.route('/seller/checkout')
def seller_checkout():
    return render_template('/seller/checkout.html')


@app.route('/seller/logout')
def seller_logout():
    logout_user()
    return redirect(url_for('home'))

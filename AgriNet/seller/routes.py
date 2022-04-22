from AgriNet import app
from flask import render_template, redirect, flash, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


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


# @app.route('/seller/login')
# def login():
#     return render_template('/seller/login.html')
#
#
# @app.route('/seller/register')
# def register():
#     return render_template('/seller/registration.html')
#
#
# @app.route('/seller/home')
# def home():
#     return render_template('/seller/index.html')
#
#
# @app.route('/seller/productview/<product_id>')
# def product(product_id):
#     return render_template('/seller/product-details.html')
#
#
# @app.route('/seller/dashboard')
# def dashboard():
#     return render_template('/seller/dashboard.html')
#
#
# @app.route('/seller/checkout')
# def checkout():
#     return render_template('/seller/checkout.html')

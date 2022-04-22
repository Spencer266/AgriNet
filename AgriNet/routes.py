from functools import wraps

from AgriNet import app
from flask import render_template, redirect, flash, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if current_user.name == role:
                return f(*args, **kwargs)
            else:
                flash("You need to be an admin to view that page.")
                return redirect(url_for('home'))
        return wrap
    return decorator


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/detail")
def details():
    return render_template('product-details.html')

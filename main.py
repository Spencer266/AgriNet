from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('test.html')


@app.route("/index.html")
def home2():
    return render_template('test.html')


@app.route("/shop-details")
def details():
    return render_template('shop-details.html')


@app.route("/shop-grid")
def shop_grid():
    return render_template('shop-grid.html')


@app.route("/shopping-cart")
def shop_cart():
    return render_template('shoping-cart.html')


@app.route("/checkout")
def checkout():
    return render_template('checkout.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)


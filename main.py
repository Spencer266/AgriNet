from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/price")
def price():
    return render_template("price-analytic.html")


if __name__ == '__main__':
    app.run(debug=True)
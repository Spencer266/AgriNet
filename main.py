from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('test.html')


@app.route("/detail")
def details():
    return render_template('shop-details.html')


if __name__ == '__main__':
    app.run(debug=True)


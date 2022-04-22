from AgriNet import app


@app.route("/price-analytic")
def price():
    return render_template('seller/price-analytic.html')


if __name__ == '__main__':
    app.run(debug=True)


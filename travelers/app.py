from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
# from databases import query_all

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/contact')
def contact_page():
	return render_template("contact.html")

@app.route('/booking')
def booking_page():
	return render_template("booking.html",items=query_all()) 

@app.route('/discount')
def discount_page():
	return render_template("discount.html")


if __name__ == '__main__':
    app.run(debug=True)
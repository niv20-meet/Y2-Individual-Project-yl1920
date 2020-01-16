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
	return render_template("booking.html") 

@app.route('/discount')
def discount_page():
	return render_template("discount.html")

@app.route('/login_page')
def login_page():
	return render_template("login.html")


@app.route('/about')
def about_page():
	return render_template("about.html")


@app.route('/blog')
def blog_page():
	return render_template("blog.html")

@app.route('/destination')
def destination_page():
	return render_template("destination.html")

if __name__ == '__main__':
    app.run(debug=True)
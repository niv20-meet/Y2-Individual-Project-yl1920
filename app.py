from databases import *
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

@app.route('/signup_page')
def signup_page():
	return render_template("signup.html")


@app.route('/about')
def about_page():
	return render_template("about.html")
 

@app.route('/blog')
def blog_page():
	return render_template("blog.html")

@app.route('/getmethod/<jsdata>')
def get_javascript_data(jsdata):
    return jsdata

@app.route('/login', methods=['POST','GET'])
def login_page():
	print(1111111111)
	if request.method == 'GET':
		print("getttttttt")
		return render_template("login1.html")
	else:
		print("postttttttt")
		username = request.form['username']
		password = request.form['password']
		user = get_user(request.form['username'])
		if user != None and request.form["password"]:
			login_session['name'] = user.username
			login_session['logged_in'] = True
			return render_template("index.html")
		else:

			return render_template("index.html")

@app.route('/signup', methods=['POST','GET'])
def signup():
	print("lol")
	#check that username isn't already taken
	username = request.form['username']
	
	usernames=[]
	users=query_all()
	for user1 in users:
		usernames.append(user1.username)


	if username not in usernames:
		print("It's available.")
		add_user(request.form['username'],request.form['password'],request.form['email'])
		return redirect(url_for("home_page"))
	return redirect(url_for('signup_page'))
	print(user)


@app.route('/logged-in' ,methods=['POST','GET'])
def logged_in():
	u = get_user(login_session['name'])

	return render_template('index.html',u=u)


@app.route('/logout')
def logout():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)
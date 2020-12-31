from flask import Flask, render_template, redirect, request


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template("login.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
	return render_template("signin.html")


@app.route('/content', methods=['GET', 'POST'])
def content():
	return render_template("content.html")







if __name__ == '__main__':
    app.run(debug = True)
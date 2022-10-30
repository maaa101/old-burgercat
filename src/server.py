from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("navbar.html") + render_template("home.html")

@app.route('/post')
def post():
    return render_template("navbar.html") + render_template("post.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=8080)
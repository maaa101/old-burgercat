import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
#from werkzeug.exceptions import abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "fart"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/post', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form["title"]
        imgurl = request.form["imgurl"]

        if not title:
            flash("do you think you can get away with posting a burger without a title")
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, imgurl) VALUES (?, ?)',
                         (title, imgurl))
            conn.commit()
            conn.close()
            return render_template("donepost.html")

    return render_template("navbar.html") + render_template("post.html")

@app.route('/')
def home():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("navbar.html") + render_template("home.html", posts=posts)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=8080)
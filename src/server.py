# the burgercat server

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
#from werkzeug.exceptions import abort

print("the burger server has started")

# trusted image sources
# this is to prevent malicous actors from harvesting IP addresses
trustedsources = ["https://cdn.discordapp.com/attachments", "https://media.discordapp.net/attachments", "https://media.tenor.com"]

app = Flask(__name__)

# the great burger key
# change it to a long string of characters
# DO NOT SHARE THIS WITH ANYONE
app.config["SECRET_KEY"] = "placeholder"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/post', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form["title"]
        imgurl = request.form["imgurl"]

        if not title:
            flash("you can't get away with posting without having a title!!!!")
        elif not imgurl:
            flash("you forgot the actual image")
        else:
            for string in trustedsources:
                if string in imgurl:
                    flash("Invalid image URL")
                    print(imgurl + " is not a trusted image URL")
                else:
                    conn = get_db_connection()
                    conn.execute('INSERT INTO posts (title, imgurl) VALUES (?, ?)', (title, imgurl))
                    conn.commit()
                    conn.close()
                    return render_template("donepost.html")

    return render_template("navbar.html") + render_template("post.html")

@app.route('/', methods=('GET', 'POST'))
def home():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created DESC;').fetchall()
    conn.close()
    if request.method == 'POST':
        id = request.form["id"]
        #print(id)
        return render_template("navbar.html") + render_template("home.html", posts=posts)
    return render_template("navbar.html") + render_template("home.html", posts=posts)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=8080)
    print("the burger server has ended")
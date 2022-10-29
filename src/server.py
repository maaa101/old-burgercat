from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    render_template("/index/home.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=8080)
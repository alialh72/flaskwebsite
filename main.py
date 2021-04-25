from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/home_<name>")
def home(name):
    return render_template("index.html", red = name)

@app.route("/")
def index():
    return "much"

if __name__ == "__main__":
    app.run()
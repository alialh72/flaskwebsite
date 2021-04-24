from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home_<name>")
def home(name):
    return render_template("index.html", red = name)

@app.route("/")
def index():
    return "much love"




if __name__ == "__main__":
    app.run()
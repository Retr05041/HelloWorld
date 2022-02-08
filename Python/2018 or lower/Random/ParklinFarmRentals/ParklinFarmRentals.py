# IMPORTS
from flask import Flask, render_template, url_for
from db import *

# INIT/CONFIG
app = Flask(__name__)

# HOME PAGE
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", posts=posts)

# ABOUT PAGE
@app.route("/about")
def about():
    return render_template("about.html")

# CONTACT PAGE
@app.route("/contact")
def contact():
    return render_template("contact.html")

# RUNS WEBSITE
if __name__ == "__main__":
    app.run(debug=True)

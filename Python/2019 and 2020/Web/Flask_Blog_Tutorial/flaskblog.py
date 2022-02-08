# --<{  Flask Blog Tutorial }>--
# --<{  https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH }>--
# --<{  Code Snippits : https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets   }>--

# PIP COMMANDS
# pip install flask - for flask
# pip install flask-wtf - for forms
# pip install email_validator - for email validation

# IMPORTS
from flask import Flask, render_template, url_for, flash, redirect # from the flask framework import the Flask Class | render_template renders HTML files (defult is .../templates/... | url_for is to find files | flash is a one time message for validation | redirect for.. you guessed it, redirecting)
from forms import RegistrationForm, LoginForm # imports from our other file

# CREATE APP
app = Flask(__name__) # makes app an instance of the Flask class
app.config["SECRET_KEY"] = "d2be469173a363415b4847ad8831bb61" # makes site secure (idk how lol)

# DUMMY DATA
posts = [ # list of dic for dummy posts
    {
        "author": "Parker Cranfield",
        "title": "Parkers First Blog Post",
        "content": "Sup Dog",
        "date_posted": "Sep. 20, 2020"
    },
    {
        "author": "Colin Cranfield",
        "title": "Colins First Blog Post",
        "content": "Not much dude",
        "date_posted": "Sep. 20, 2020"
    }
]

# ROUTES
@app.route("/") # routes for our website (ex. blog:5000/home) - "/" is what is run first
@app.route("/home") # adds another way to get to this page
def home(): # creates page function
    return render_template("home.html", posts=posts) # returns to the browser | any var given will be "{var name used in HTML}={var name of thing to be sent}"

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"]) # added get and post so it can accept them from browser
def register():
    form = RegistrationForm() # makes an instance of the form class as form
    if form.validate_on_submit(): # if no errors pop up when the form is submited
        flash(f"Account created for {form.username.data}!", "success") # flashed message - look for in layout.html
        return redirect(url_for("home")) # takes us to home function up top
    return render_template("register.html", title="Register", form=form) # notice how we send the form to the html doc

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "abc123":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__": # runs server
    app.run("0.0.0.0", debug=True) # if left without an IP it will only run on localhost, 0.0.0.0 means anyone on network can see it, 8000 is port, debug means live editing
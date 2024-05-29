import os

# importing the necessary functions like render_template, SQL, etc, so they can be used in the code
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# used phpliteadmin to create table
# type in "phpliteadmin kdramas.db" to view the users table and info
db = SQL("sqlite:///kdramas.db")

# app routes rendering HTML templates when the url is used
@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@app.route("/iconicscenes")
def iconicscenes():
    return render_template('iconicscenes.html')

@app.route("/richboypoorgirl")
def richboypoorgirl():
    return render_template('richboypoorgirl.html')

@app.route("/richgirlpoorboy")
def richgirlpoorboy():
    return render_template('richgirlpoorboy.html')

@app.route("/friendstolovers")
def friendstolovers():
    return render_template("friendstolovers.html")

@app.route("/lovetriangle")
def lovetriangle():
    return render_template('lovetriangle.html')

@app.route("/contractrelationship")
def contractrelationship():
    return render_template('contractrelationship.html')

# ensure that responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# app routing for dashboard page, where user must be logged in
# Login/logout/register from finance
@app.route("/dashboard", methods=["POST","GET"])
@login_required
def dashboard():
    """Allows users to see their username and favorite kdramas, as well as update their favorite kdrama"""
    # Using POST means that data will not be stored in URL and that data will be resubmitted
    # if the form on the dashboard page (meaning user updated their favorite kdrama), the newfavoritekdrama variable is what the user inputted
    if request.method == "POST":
        # the "newfavoritekdrama" references in the id of the user's input in dashboard.html
        newfavoritekdrama = request.form.get("newfavoritekdrama")
        # in the user SQL table, sets the favoritekdrama row to the kdrama that the user inputted
        # the WHERE conditional ensures that the right user's favorite kdrama is being updated and not another user's
        db.execute("UPDATE users SET favoritekdrama=? WHERE id=?", newfavoritekdrama, session["user_id"])
    # even if no new favorite kdrama was updated, the favoritekdrama column in dashboard is the user's current favorite kdrama
    favoritekdrama = db.execute("SELECT favoritekdrama, username FROM users where id = ?", session["user_id"])

    return render_template("dashboard.html", favoritekdrama=favoritekdrama)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation password")
        # Also ensures that two of the same usernames are not registered
        # if the input in the password field does not match the input in the confirmation field, call the apology function saying that the passwords must match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match")

        # If the length of the password that the user inputs is less than 8, return apology with message
        if len(request.form.get("password")) < 8:
            return apology("password must be 8 characters at least")

        # users must enter their favorite kdrama to register
        if not request.form.get("favoritekdrama"):
            return apology("must provide favorite kdrama")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 0:
            return apology("duplicate username")

        # insert new user into database, call generate_password_hash function, update the user's favoritekdrama in the SQL table
        db.execute("INSERT INTO users (username, hash, favoritekdrama) VALUES (?, ?, ?)", request.form.get(
            "username"), generate_password_hash(request.form.get("password")), request.form.get("favoritekdrama"))

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")







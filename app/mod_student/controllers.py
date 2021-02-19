from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from pip._internal.network import session
from werkzeug.security import generate_password_hash, check_password_hash

# Change dbname here
db_name = "auth.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SECRET_KEY required for session, flash and Flask Sqlalchemy to work
app.config['SECRET_KEY'] = 'configure strong secret key here'
db = SQLAlchemy(app)

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    pass_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '' % self.username

def create_db():
    """ # Execute this first time to create new db in current directory. """
    db.create_all()

mod_student = Blueprint('student', __name__, url_prefix='/Student')

@mod_student.route('/index/', methods =['GET', 'POST'])
def index():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Username or Password cannot be empty")
            return redirect(url_for('student/index.html'))
        else:
            username = username.strip()
            password = password.strip()

        # Returns salted pwd hash in format : method$salt$hashedvalue
        hashed_pwd = generate_password_hash(password, 'sha256')

        new_user = User(username=username, pass_hash=hashed_pwd)
        db.session.add(new_user)

        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            flash("Username {u} is not available.".format(u=username))
            return redirect(url_for('student/index.html'))

        flash("User account has been created.")
        return redirect(url_for("student/login.html"))

    return render_template('student/index.html')

@mod_student.route('/', methods =['GET', 'POST'])
@mod_student.route('/login/', methods =['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Username or Password cannot be empty.")
            return redirect(url_for('student/login.html'))
        else:
            username = username.strip()
            password = password.strip()

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.pass_hash, password):
            session[username] = True
            return redirect(url_for("user_home", username=username))
        else:
            flash("Invalid username or password.")

    return render_template('student/login.html')

@mod_student.route("/user/<username>/")
def user_home(username):
    """
    Home page for validated users.
    """
    if not session.get(username):
        abort(401)

    return render_template("student/user_home.html", username=username)

@mod_student.route("/logout/<username>")
def logout(username):
    """ Logout user and redirect to login page with success message."""
    session.pop(username, None)
    flash("successfully logged out.")
    return redirect(url_for('student/login.html'))
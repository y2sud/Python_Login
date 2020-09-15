from flask import Blueprint, render_template, redirect, url_for, session, request, flash, abort

from .model import Model
from .cryp import Cryp

main = Blueprint('main', __name__)

@main.route('/')
def index():
    #return render_template('signup.html')
    return redirect(url_for('main.login'))
    #return render_template('login.html')

@main.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if 'user' in session:
        error = 'Please logout from previous session'
    else:
        # user & password entered
        if request.method == 'POST':
        #if 'user' in request.form and 'psw' in request.form:
            user = request.form['user']
            password = request.form['psw']
            user_valid = Model.user_exists(user, password)
            if user_valid == 0:
                session['user'] = user
                return redirect(url_for('main.profile', user=user))
            elif user_valid == 1:
                error = "Incorrect password for " + user
            else:
                error = "Invalid user"


    return render_template('login.html', error=error)
    #return 'Hello'

@main.route('/new', methods=['POST', 'GET'])
def new():
    #abort_func(request.method, 400)
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['psw']
        email = request.form['email']
        fullname = request.form['fullname']
        add_success = Model.add_user(*(email, user, password, fullname))
        #add_success = True
        #print(add_success)
        if add_success == 0:
            flash("Signup successful! You can go back to login screen")
        elif add_success == 1:
            flash("User " + user + " already exists")
        else:
            flash("Severe error encountered during signup")
    return render_template('signup.html')

@main.route('/profile/<user>')
def profile(user=None, methods=['GET']):
    #uname = "messi"
    if 'user' not in session:
        abort_func(request.method, 403)
    fullname = Model.get_fullname(user)
    return render_template('profile.html', fname=fullname)

@main.route('/logout', methods=['GET', 'POST'])
def logout():
    abort_func(request.method, 400)
    session.pop('user', None)
    flash('You have been successfully logged out!')
    return redirect(url_for('main.login'))


def abort_func(method, code):
    if method == 'GET':
        abort(code)
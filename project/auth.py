from flask import Blueprint,render_template,redirect,url_for,request,flash
import validators
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required
from . import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        remember= True if request.form.get('remember') else False

        user = User.query.filter_by(username=username).first()

        if not user:
            print('user')
        #check if the user exists in db
        # take the user supplied and hash it. compare the hash password in database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again')
            return redirect(url_for('auth.login')) # if the user does not exist or password is wrong, reload the page
        # if the above checks passes, then weknow the user has right credentials
        
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))
    else:
        return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username=request.form.get('username')
        name=request.form.get('name')
        password=request.form.get('password')

        # check if the username exists in the database
        user = User.query.filter_by(username=username).first()

        if user: # if the username exist, redirect that back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        #create a new user with the form data. hash the password
        new_user = User(username=username,name=name, password=generate_password_hash(password,method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

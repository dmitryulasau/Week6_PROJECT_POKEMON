from flask import Blueprint, render_template, request, flash, redirect, url_for

from website import views
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect passwprd", category='error')
        else:
            flash("Email does not exist", category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')

        elif len(email) < 4:
            flash('Email must be grater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be grater than 1 character', category='error')
        elif len(last_name) < 2:
            flash('Last name must be grater than 1 character', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match', category='error')
        elif len(password) < 3:
            flash('Password must be at lest 3 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', category='success')

            return redirect(url_for('views.home'))

   
        

    return render_template('register.html', user=current_user)
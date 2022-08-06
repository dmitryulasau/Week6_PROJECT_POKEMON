from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('login.html', text="Testing")

@auth.route('/logout')
def logout():
    return "<p>LOGOUT</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    data = request.form
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if len(email) < 4:
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
            flash('Registration successful!', category='success')

   
        

    return render_template('register.html')
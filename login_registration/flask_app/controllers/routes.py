from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new', methods=['POST'])
def log_new_user():
    if user.User.validate_user(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        print(data)
        user_id = user.User.save(data)
        session['user_id'] = user_id
        return redirect('success')
    return redirect('/')

@app.route('/success')
def success():
    if 'user_id' in session:
        return render_template('success.html')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    this_user =user.User.get_by_email(request.form)
    print(request.form)
    if this_user:
        if bcrypt.check_password_hash(this_user.password, request.form['password']):
            session['user_id'] = this_user.id
            return redirect ('/success')
    flash('Invalid credentials!', 'login')
    return redirect ('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
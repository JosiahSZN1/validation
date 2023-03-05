from flask_app import app
from flask import render_template,redirect,request,session


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_pw': request.form['confirm_pw'] 
    }
    
    return redirect()
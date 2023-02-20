from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import order

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def show_orders():
    order.Order.get_all()
    return render_template('index.html', all_orders = order.Order.get_all())

@app.route('/cookies/new')
def new_order():
    return render_template('order.html')

@app.route('/cookies/new/log', methods=['POST'])
def log_new_order():
    data = {
        'name': request.form['name'],
        'cookie_type': request.form['cookie_type'],
        'num_boxes': request.form['num_boxes']
    }
    print(data)
    if not order.Order.validate_order(request.form):
        return redirect('/cookies/new')
    order.Order.save(data)
    return redirect('/cookies')

@app.route('/cookies/edit/<int:id>')
def edit_order(id):
    return render_template('edit.html', order_info = order.Order.get_one({'id': id}))

@app.route('/cookies/edit/<int:id>/log', methods=['POST'])
def log_edit_order(id):
    data = {
        'id': id,
        'name': request.form['name'],
        'cookie_type': request.form['cookie_type'],
        'num_boxes': request.form['num_boxes']
    }
    if not order.Order.validate_order(request.form):
        return redirect('/cookies/edit')
    order.Order.update(data)
    return redirect('/cookies')
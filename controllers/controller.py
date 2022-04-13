from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title="Pizza Orders", order_list= orders)

@app.route('/orders/<index>')
def order(index):
    order = orders[int(index)]
    return render_template('order.html', title=f"Order no: {order}", order = order)


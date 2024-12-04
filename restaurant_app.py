from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///order.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    orders = db.Column(db.String(500), nullable=False)
    table_number = db.Column(db.Integer, nullable=False)

# Routes
@app.route('/')
def home():
    return redirect(url_for('main_menu', table_number=1))

@app.route('/<int:table_number>', methods=['GET'])
def main_menu(table_number):
    return render_template('main_menu.html', table_number=table_number)

@app.route('/order/<int:table_number>', methods=['POST'])
def order(table_number):
    customer_name = request.form.get('customer_name')
    order_summary = request.form.get('order_summary')
    new_order = Order(customer_name=customer_name, orders=order_summary, table_number=table_number)
    db.session.add(new_order)
    db.session.commit()
    return render_template('order_summary.html', customer_name=customer_name, table_number=table_number, orders=order_summary)

@app.route('/kitchen/', methods=['GET'])  #for testing: http://127.0.0.1:5000/kitchen/
def kitchen():
    orders = Order.query.all()
    return render_template('kitchen.html', orders=orders)

@app.route('/delete/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
    return redirect(url_for('kitchen'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

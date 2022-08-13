from flask import Flask, json, request, flash, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

DB_URI = "postgresql+psycopg2://user02:peserta_user02@35.222.132.160:5432/postgres"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Users(db.Model):
    __table_args__ = {"schema": "althaf"}
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    telp = db.Column(db.String(14))

class Products(db.Model):
    __table_args__ = {"schema": "althaf"}
    id = db.Column('product_id', db.Integer, primary_key = True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.String(10))

class Orders(db.Model):
    __table_args__ = {"schema": "althaf"}
    id = db.Column('Order_id', db.Integer, primary_key = True)
    date_order = db.Column(db.Date)  



@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        users = Users.query.all()
        results = [{"id": u.id, "name": u.name, "city": u.city, "telp": u.telp } for u in users]
        return jsonify(results)

    elif request.method == 'POST':
        user = Users(
            name=request.form['name'],
            city=request.form['city'],
            telp=request.form['telp']
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'ok'})

    else:
        return 'Method not allowed'

@app.route("/user/<id>", methods=['GET'])
def user_by_id(id):
    users = Users.query.filter_by(id=id)
    results = [{"id": u.id, "name": u.name, "city": u.city, "telp": u.telp } for u in users]
    return jsonify(results)

@app.route('/product', methods=['GET', 'POST'])
def product():

    if request.method == 'GET':
        products = Products.query.all()
        results = [{"id": u.id, "product_name": u.product_name, "price": u.price} for u in products]
        return jsonify(results)

    elif request.method == 'POST':
        product=Products(
            product_name=request.form['product_name'],
            price =request.form['price']
        )
        db.session.add(product)
        db.session.commit()
        return jsonify ({'status':'ok'})

    else:
        return 'Method not allowed'

@app.route("/product/<id>", methods=['GET'])
def product_by_id(id):
    products = Products.query.filter_by(id=id)
    results = [{"id": u.id, "product_name": u.product_name, "price": u.price} for u in products]
    return jsonify(results)


@app.route('/order', methods=['GET', 'POST'])
def order():

    if request.method == 'GET':

        orders = Orders.query.all()
        results = [{"id": u.id, "date_order": u.date_order} for u in orders]
        return jsonify(results)

    elif request.method == 'POST':

        order = Orders(
            date_order=request.form['date_order'],
        )
        db.session.add(order)
        db.session.commit()
        return jsonify({'status': 'ok'})

    else:
        return 'Method not allowed'

@app.route("/order/<id>", methods=['GET'])
def order_by_id(id):
    orders = Orders.query.filter_by(id=id)
    results = [{"id": u.id, "date_order": u.date_order} for u in orders]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug = True)
    db.create_all()








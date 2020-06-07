from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient



client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('homework_1_donghan.html')

@app.route('/orders', methods=['POST'])
def write_order():
    user_receive = request.form['user_give']
    phone_receive = request.form['phone_give']
    period_receive = request.form['period_give']

    order = {
        'user': user_receive,
        'phone': phone_receive,
        'period': period_receive 
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg':'주문이 성공적으로 완료되었습니다!'})

@app.route('/orders', methods=['GET'])
def show_order():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

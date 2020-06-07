from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    weight_receive = request.form['weight_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    orders = {'name':name_receive, 'weight':weight_receive, 'address':address_receive, 'number':number_receive}
    db.week4hw.insert_one(orders)

    return jsonify({'result':'success', 'msg': '주문 완료'})


@app.route('/order', methods=['GET'])
def read_reviews():
    orders = list(db.week4hw.find({},{'_id':0}))
    return jsonify({'result':'success', 'msg': '환영합니다','orders':orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
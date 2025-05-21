from flask import Flask ,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB 設定（改成你的 URI）
app.config["MONGO_URI"] = "mongodb://localhost:27017/iamdb"
mongo = PyMongo(app)

@app.route("/")
def index():
    #mongo.test_collection.insert_one({'msg': 'Hello from Flask and MongoDB'})
    # 從資料庫讀取一筆資料
    doc = mongo.db.users.find()
    users = list(doc)
    for u in users:
        u["_id"] = str(u["_id"])  # ObjectId 轉字串

    return jsonify({"users": users})

@app.route("/add_user")
def add_user():
    user = {"username": "alice", "password": "123456", "role": "admin"}
    mongo.db.users.insert_one(user)
    return "User inserted!"

@app.route("/users")
def get_users():
    users = list(mongo.db.users.find({}, {"_id": 0}))
    return {"users": users}

if __name__ == "__main__":
    app.run(debug=True)
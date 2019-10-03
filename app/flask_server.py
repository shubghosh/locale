from flask import Flask, request
import hashlib
import json
from q_management import sender as q
from q_management import db_config as db

app = Flask(__name__)


@app.route("/savedata", methods=["POST"])
def log_request():
    # data = json.loads(request.data.decode('utf-8'))
    data = request.data
    if data:
        print("Request Logged")
    else:
        return "Request Not Logged"
    result = hashlib.md5(str(data).encode())
    md5 = result.hexdigest()
    data = json.loads(data)
    data["md5"] = md5
    q.start_queuing(json.dumps(data))
    return "request is logged with id " + md5


@app.route("/fetchdata", methods=["POST"])
def fetch_record():
    # data = json.loads(request.data.decode('utf-8'))
    data = json.loads(request.data)
    print(data)
    resp = db.fetch_record(data['md5'])
    return resp

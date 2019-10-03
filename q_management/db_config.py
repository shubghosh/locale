from pymongo import MongoClient
import json

conn = MongoClient()
db = conn["locale"]
col = db["rides"]


def fetch_record(id):
    try:
        data_dict = {}
        record = col.find({"md5": id}, {"_id": 0})
        for r in record:
            data_dict = r
        if data_dict:
            return json.dumps(data_dict)
        else:
            return "Request is logged...Check after sometime"
    except Exception as e:
        print(e)
        return "Request is logged...Check after sometime"


def insert_record(data):
    try:
        col.insert_one(data)
    except Exception as e:
        print(e)
        print(data["md5"])

import requests
import sys
import json
url = "http://127.0.0.1:5000/fetchdata"


def fetch_record(id):
    data_dict = json.dumps({"md5": id})
    response = requests.post(url, data=data_dict)
    if response.status_code != 200:
        print("Failed to load response")
    print(response.text)


if __name__ == "__main__":
    if sys.argv[1]:
        fetch_record(sys.argv[1])
    else:
        print("Please enter record id")

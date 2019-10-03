import requests
from csv import DictReader
import json

the_reader = DictReader(open("../Data.csv", "r"))
url = "http://127.0.0.1:5000/savedata"
for line_dict in the_reader:
    data_dict = {}
    for k, v in line_dict.items():
        data_dict[k] = v
    data_dict = json.dumps(data_dict)
    response = requests.post(url, data=data_dict)
    print(response)
    print(response.text)
    print("---------------------------------------------------")
    # break

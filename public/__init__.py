import random

import requests
import json
import pprint

url = "http://jadeite.migu.cn:7090/search/v3/open-search/"

payload = json.dumps({
    "k": "我爱你",
    "pageIdx": 1,
    "searchScene": 10,
    "pageSize": 10,
    "appVersion": "2.27.0.20230703",
    "ct": 301
})

payload1 = json.dumps({
    "k": "啦啦啦啦啦",
    "pageIdx": 1,
    "searchScene": 10,
    "pageSize": 10,
    "appVersion": "2.27.0.20230703",
    "ct": 301
})
headers = {
    'Content-Type': 'application/json'
}

for i in range(1, 100):
    if i % 2 == 0:
        response = requests.request("POST", url, headers=headers, data=payload)

        pprint.pprint(len(response.json().get("body").get("contDisplayTypeList")))
    else:
        response = requests.request("POST", url, headers=headers, data=payload1)

        pprint.pprint(len(response.json().get("body").get("contDisplayTypeList")))


        random.Random
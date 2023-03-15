import requests
import json

data = {
    'no' : 1,
    'result' : '所有URL爬取完成'
}
headers = {'Content-Type': 'application/json'}
url = 'http://38.21.244.19:13435/bugstore'
conn = requests.post(url=url, json = json.dumps(data),headers=headers)
print("发送状态" + str(conn.status_code))
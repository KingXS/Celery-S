from celery_app import task1
from celery_app import task2


import time
from celery_app import app
import redis
import queue
import simplejson
import threading
import subprocess
import requests
import warnings
import json

#任务1测试
file = open("targets.txt")
for text in file.readlines():
    data1 = text.strip('\n')
    re = task1.crawlurls.delay(data1)
    print(re.get())
print("爬取完成")


data = {
    'no' : 1,
    'result' : '所有URL爬取完成'
}
headers = {'Content-Type': 'application/json'}
url = 'http://103.143.11.144:13435/bugstore'
conn = requests.post(url=url, json = json.dumps(data),headers=headers)
print("发送状态" + str(conn.status_code))


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



num = 0

r = redis.Redis(host='103.143.11.184',password = '',port = 6379,db = 1)
for url in r.hkeys('crawler_results'):
    result = r.hget('crawler_results',url)
    x = json.loads(result)
    #url1 = x['url']
    re = task2.niupiscan.delay(x)
    num = num + 1
    print(re.get())
    time.sleep(2)



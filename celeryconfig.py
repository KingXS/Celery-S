from celery.schedules import crontab
from datetime import timedelta
from kombu import Queue
from kombu import Exchange
from urllib.parse import quote_plus



result_serializer = 'json'

#需要对密码进行编码处理
PASSWORD1 = quote_plus('')
PASSWORD2 = quote_plus('')

broker_url = 'redis://:{}@103.143.11.144/1'.format(PASSWORD1)  #美国D1
result_backend = 'redis://:{}@103.143.11.183/1'.format(PASSWORD2)   #美国D3
timezone = "America/Los_Angeles"
imports = (
    'celery_app.task1',
    'celery_app.task2'
)

#定时执行
#beat_schedule = {
    #'add-every-20-seconds': {
    #    'task': 'celery_app.task1.crawlurls',
    #    'schedule': timedelta(seconds=)
        #'args': (5, 7)
    #},
    #'add-every-10-seconds': {
    #    'task': 'celery_app.task2.add',
    #     'schedule': crontab(hour=9, minute=10),
    #    'schedule': timedelta(seconds=10),
    #    'args': (23, 54)
    #}
#}

task_queues = (
    Queue('default', exchange=Exchange('default'), routing_key='default'),
    Queue('priority_high', exchange=Exchange('priority_high'), routing_key='priority_high'),
    Queue('priority_low', exchange=Exchange('priority_low'), routing_key='priority_low'),
)

task_routes = {
    'celery_app.task1.crawlurls': {'queue': 'priority_high', 'routing_key': 'priority_high'},
    'celery_app.task2.niupiscan': {'queue': 'priority_low', 'routing_key': 'priority_low'},
}

# 每分钟最大速率
# task_annotations = {
#     'task2.multiply': {'rate_limit': '10/m'}
# }


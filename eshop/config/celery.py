import os
from celery import Celery
from kombu import Exchange, Queue


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")


# allocating self-queues to each celery worker without using message brokers for test (optional)

# app.conf.task_routes={
#     'notifications.tasks.send_discount_emails':{'queue':'queue1'},
#     'notifications.tasks.process_data_for_ml':{'queue':'queue2'},
# }


# public tasks rate limit 
# app.conf.task_default_rate_limit='1/m'



# Redis Message Broker conf
# queues=>celery,celery:1,celery:2,celery:3
# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }





# Rabbit Message Broker conf

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]
app.conf.task_acks_late=True
app.conf.task_default_priority=5
app.conf.worker_prefetch_multiplier=1
app.conf.workerconcurrency=1

    

app.autodiscover_tasks()



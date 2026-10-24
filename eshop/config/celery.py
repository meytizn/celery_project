import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")


# allocating self-queues to each celery worker without using message brokers for test (optional)

# app.conf.task_routes={
#     'notifications.tasks.send_discount_emails':{'queue':'queue1'},
#     'notifications.tasks.process_data_for_ml':{'queue':'queue2'},
# }



# allocating redis queues to internal celery worker (Redis Message Broker )

# queues=>celery,celery:1,celery:2,celery:3
app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}

app.autodiscover_tasks()
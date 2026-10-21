from celery import Celery

app=Celery('tasks')
app.config_from_object('celery_config')

# tasks routes queues standalone
app.conf.imports=('notifications.tasks',)
app.autodiscover_tasks()

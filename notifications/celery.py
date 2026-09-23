
import os
from celery import Celery


# celery configuration service to be run beside project

  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
  app = Celery('config')
  app.conf.from_object('django.conf:settings',namespace='CELERY')
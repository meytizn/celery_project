from celery import shared_task
import time


#the tasks using redis queues (celery,celery:1,celery:2,celery:3)

# private task rate limit 
@shared_task(rate_limit='1/m')
def task_1(queue='celery'):
    time.sleep(3)
    return


@shared_task
def task_2(queue='celery:1'):
    time.sleep(3)
    return


@shared_task
def task_3(queue='celery:2'):
    time.sleep(3)
    return


@shared_task
def task_4(queue='celery:3'):
    time.sleep(3)
    return


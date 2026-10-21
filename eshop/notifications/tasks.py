from celery import shared_task


@shared_task
def send_discount_emails():
    print("send_discount_emails done from queue1 ! ")

@shared_task
def process_data_for_ml():
    print("process_data_for_ml done from queue2 !")
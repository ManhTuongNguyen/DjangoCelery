from time import sleep
from celery import shared_task
import logging


@shared_task()
def heavy_task():
    logging.info('Starting heavy_task')
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    print('Ahihi')
    return 5

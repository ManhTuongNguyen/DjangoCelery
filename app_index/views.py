import logging
from django.http import HttpResponse
from .tasks import heavy_task


def index(request):
    logging.info('Starting index view')
    heavy_task.delay()
    logging.info('Called heavy_task.delay()')
    return HttpResponse('Done!')

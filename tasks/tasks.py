import requests
from celery import shared_task

from tasks.models import Task


@shared_task
def send_notification(*args, **kwargs):
    if kwargs.get('url'):
        response = requests.post(kwargs['url'])
        Task.objects.create(
            status_code=response.status_code,
            response=response.json(),
            url=kwargs['url']
        )
        print('Notification sent')
    else:
        raise ValueError('You must have set the\
            url in "Keyword Arguments" field')

import os

import django_rq
from app.utils import generate_check_task


def generate_check(sender, instance, created, **kwargs):
    if created:
        try:
            os.fork()
            django_rq.enqueue(generate_check_task, instance)
        except:
            generate_check_task(instance)


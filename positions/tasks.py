from datetime import timedelta

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task

from .models import Test
from .utils import get_random_code


@shared_task
def create_test_obj(name):
    Test.objects.create(name=name)


@shared_task
def create_signals_code():
    tests = Test.objects.all()
    for test in tests:
        test.code = get_random_code()
        test.save()


@periodic_task(run_every=(crontab(minute='*/1')))
def run_create_objects():
    create_test_obj.delay(name='create_obj')

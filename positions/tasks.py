from datetime import timedelta

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task

from .models import Test


@shared_task
def create_test_obj(name):
    Test.objects.create(name=name)


@periodic_task(run_every=timedelta(seconds=3))
def ren_create_objects():
    create_test_obj.delay(name='create_obj')


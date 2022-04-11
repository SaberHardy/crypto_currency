from datetime import timedelta

import requests
from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task

from .models import Test, Position
from .utils import get_random_code


@shared_task
def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=' \
          'USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'

    all_data = requests.get(url).json()

    for item in all_data:
        p, _ = Position.objects.get_or_create(name=item['name'], )
        p.image = item['image']
        p.price = item['current_price']
        p.rank = item['market_cap_rank']
        p.market_cap = item['market_cap']

        p.save()


@periodic_task(run_every=(crontab(minute='*/1')))
def get_crypto_current():
    get_crypto_data.delay()

# @shared_task
# def create_test_obj(name):
#     Test.objects.create(name=name)
#
#
# @shared_task
# def create_signals_code():
#     tests = Test.objects.all()
#     for test in tests:
#         test.code = get_random_code()
#         test.save()
#
#
# @periodic_task(run_every=(crontab(minute='*/1')))
# def run_create_objects():
#     create_test_obj.delay(name='create_obj')

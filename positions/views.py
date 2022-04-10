import requests
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=' \
          'USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'

    all_data = requests.get(url).json()
    context = {
        'all_data': all_data,
    }
    return render(request, 'positions/main.html', context)

import asyncio
import aiohttp
import requests
from django.conf import settings
from django.utils import timezone

from core.models import Website, Crypto


async def update_websites_status():
    websites = Website.objects.all()
    for website in websites:
        async with aiohttp.request(method='GET', url=website.url) as r:
            website.status = str(r.status)
            website.status_changed = timezone.now()
            website.save()


async def api_update_currencies():
    headers = {
        'X-CMC_PRO_API_KEY': settings.CMC_API_KEY,
    }
    params = {
        'qs': {
            'start': 1,
            'limit': 5,
            'convert': 'USD',
        },
        'json': True,
        'gzip': True,
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', data=params) as r:
            response = await r.json()
            currencies = response.get('data', [])
            for currency in currencies:
                try:
                    crypto, created = Crypto.objects.get_or_create(name=currency.get('symbol').lower())
                    crypto.current_rate = currency.get('quote', {}).get('USD', {}).get('price', None)
                    crypto.rate_changed = timezone.now()
                    crypto.save()
                except Exception as ex:
                    print(ex)

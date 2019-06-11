import telepot

from django.conf import settings


def get_bot():
    return telepot.Bot(settings.BOT_TOKEN)

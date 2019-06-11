import time

import telepot
from django.conf import settings
from django.core.management.base import BaseCommand
from telepot.loop import MessageLoop

from bot.handler import handle


class Command(BaseCommand):
    help = 'Starts telegram chat bot messageloop'

    def handle(self, *args, **options):
        bot = telepot.Bot(settings.BOT_TOKEN)
        MessageLoop(bot, handle).run_as_thread()

        while 1:
            time.sleep(10)

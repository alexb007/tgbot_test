from bot.utils import get_bot
from core.models import Crypto
from django.conf import settings

bot = get_bot()


def get_currencies(chat_id):
    currencies = Crypto.objects.filter(current_rate__isnull=False)
    text = 'Currently these currencies available\n' if currencies else 'No available currency'
    for currency in currencies:
        text += settings.BOT_CURRENCY_FORMAT.format(name=currency.name.upper(), rate=currency.current_rate)
        text += '\n'

    bot.sendMessage(chat_id, text)


def get_currency(chat_id, currency_code):
    try:
        currency = Crypto.objects.get(name=currency_code.lower())
        text = settings.BOT_CURRENCY_FORMAT.format(name=currency.name.upper(), rate=currency.current_rate)
    except Crypto.DoesNotExist:
        text = 'This Crypto Currency is not exists! Create your own.'
    bot.sendMessage(chat_id, text)


COMMANDS = {
    'get_currencies': get_currencies,
    'get_currency': get_currency,
}

NAMED_COMMANDS = {
    'All currencies': get_currencies,
}


def get_command(command):
    return COMMANDS.get(command, None) or NAMED_COMMANDS.get(command, None)


def is_command(msg):
    command_text = msg.lstrip('/')
    return command_text in NAMED_COMMANDS or (msg.startswith('/') and command_text in COMMANDS)

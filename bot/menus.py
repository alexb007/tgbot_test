from django.conf import settings
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

from bot.utils import get_bot
from core.models import Crypto

bot = get_bot()


def start(chat_id):
    currencies = Crypto.objects.filter(current_rate__isnull=False).order_by('name', 'rate_changed')
    keyboard_buttons = [
        [KeyboardButton(text='All currencies')],
    ]
    for currency in currencies:
        keyboard_buttons.append([KeyboardButton(text=currency.name.upper())])
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_buttons)
    bot.sendMessage(chat_id, settings.BOT_WELCOME, reply_markup=keyboard)


MENUS = {
    'start': start,
}


def is_menu(msg):
    msg = msg.lstrip('/')
    return msg.lower() in MENUS.keys()


def get_menu(menu_name):
    return MENUS.get(menu_name)

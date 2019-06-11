import telepot
from django.utils.translation import ugettext_lazy as _

from bot.menus import get_menu, is_menu
from bot.utils import get_bot
from bot.commands import get_command, is_command
from core.models import Crypto

bot = get_bot()


def handle_command(command_name, chat_id):
    command_name = command_name.lstrip('/')
    command = get_command(command_name)
    if command and callable(command):
        command(chat_id)


def handle_menu(menu_name, chat_id):
    menu_name = menu_name.lstrip('/')
    menu = get_menu(menu_name)
    if menu and callable(menu):
        menu(chat_id)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        text = msg.get('text', None)
        if is_command(text):
            handle_command(command_name=text, chat_id=chat_id)
        elif is_menu(text):
            handle_menu(menu_name=text, chat_id=chat_id)
        elif Crypto.objects.filter(name=msg['text'].lower()).exists():
            get_crypto = get_command('get_currency')
            get_crypto(chat_id, msg['text'])
        else:
            bot.sendMessage(chat_id, 'Unknown command. Do you know what you mean?')

from django.core.management.base import BaseCommand, CommandError
import os
import telebot
from django.utils import timezone
from telebot import types

from mybot.models import TelegramUser

bot = telebot.TeleBot(os.getenv('TELEGRAMKEY'))


@bot.message_handler(commands=['start'])
def start_comm(message):
    if message.from_user.first_name:
        fn = message.from_user.first_name
    else:
        fn = '-'
    if message.from_user.last_name:
        ln = message.from_user.last_name
    else:
        ln = '-'
    try:
        TelegramUser.objects.create(
            first_name=fn,
            last_name=ln,
            chat_id=message.chat.id,
            last_message=timezone.now()

        )
    except:
        pass
    bot.send_message(message.chat.id, 'Я бот, дратути', reply_markup=main_keyboard)


main_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
main_keyboard.add(types.KeyboardButton(text='python tests'), types.KeyboardButton(text='anegdot'))


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):

    if message.text == 'python tests':
        python_quize(message.chat.id)
    elif message.text == 'anegdot':
        pass
    else:
        bot.send_message(message.chat.id, 'Ne udachno')


def python_quize(chatid):
    kbd = types.InlineKeyboardMarkup()
    kbd.add(types.InlineKeyboardButton(text='ответ1', callback_data='quize_answer_1'))
    kbd.add(types.InlineKeyboardButton(text='ответ2', callback_data='quize_answer_2'))
    kbd.add(types.InlineKeyboardButton(text='ответ3', callback_data='quize_answer_3'))
    bot.send_message(chatid, '''
    какой-то вопрос''', reply_markup=kbd)


@bot.callback_query_handler(func=lambda m: True)
def quize_answer(message):
    print(message.data)
    bot.send_message(message.from_user.id, 'dgfgfhfhgh')

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print("я команда")
        bot.infinity_polling()

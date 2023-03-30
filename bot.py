5556326343:AAHMYo57MOTuVQ8zZl44N958A_QXVG6Bayc

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# функция-обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Если ты Антон, то у тебя маленькая пиписька")

# функция-обработчик для эхо-ответов на сообщения пользователя
def echo(update, context):
    update.message.reply_text(update.message.text)

# создаем объект для взаимодействия с Telegram API
bot = telegram.Bot(token='5556326343:AAHMYo57MOTuVQ8zZl44N958A_QXVG6Bayc')

# создаем объект Updater
updater = Updater(token='5556326343:AAHMYo57MOTuVQ8zZl44N958A_QXVG6Bayc', use_context=True)

# создаем обработчики команд и сообщений
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

# запускаем обработчики команд и сообщений
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(echo_handler)

# запускаем бота
updater.start_polling()
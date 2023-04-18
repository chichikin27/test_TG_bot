# 5556326343:AAHMYo57MOTuVQ8zZl44N958A_QXVG6Bayc

import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Задаем токен бота
TOKEN = '5556326343:AAHMYo57MOTuVQ8zZl44N958A_QXVG6Bayc'

# Создаем объект бота
bot = telegram.Bot(token=TOKEN)

# Функция, которая будет вызываться при получении сообщения
def reply_300(update, context):
    # Отвечаем на сообщение числом 300
    update.message.reply_text('Отсоси у тракториста))0)')

# Создаем объект для получения обновлений от Telegram
updater = Updater(token=TOKEN, use_context=True)

# Получаем диспетчер для обработки сообщений
dispatcher = updater.dispatcher

# Создаем обработчик сообщений
message_handler = MessageHandler(Filters.text, reply_300)

# Регистрируем обработчик в диспетчере
dispatcher.add_handler(message_handler)

# Запускаем бота
updater.start_polling()
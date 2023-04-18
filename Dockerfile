# Используем базовый образ Python
FROM python:3.9

# Устанавливаем необходимые зависимости
RUN pip install python-telegram-bot

# Копируем исходный код внутрь контейнера
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем бота при старте контейнера
CMD ["python", "bot.py"]
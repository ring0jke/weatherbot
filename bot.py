import telebot
import requests
import request
import aviation
from datetime import datetime

bot = telebot.TeleBot(, parse_mode=None)
r = requests.get('https://api.weather.yandex.ru/v2/forecast?')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.reply_to(message,"Напиши ICAO код аэропорта.")
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'{current_time} Metar request for: {message.text} Username: {message.from_user.username}')
        bot.reply_to(message,aviation.getMetar(message.text))

bot.polling(none_stop=True, interval=0)

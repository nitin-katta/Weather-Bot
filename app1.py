import requests 
import json
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

API_KEY = "your api-key" 

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)

    weather = data['weather'][0]['main']
    temp = round(data['main']['temp'] - 273.15,2)

    return f'The weather in {city} is {weather} with a temperature of {temp}°C'

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am a weather bot. Send me the name of a city and I will tell you the weather there.')

def weather(update: Update, context: CallbackContext):
    city = update.message.text
    weather_data = get_weather(city)
    update.message.reply_text(weather_data)

def error(update: Update, context: CallbackContext):
    update.message.reply_text('Sorry, I could not understand that city name.')

def main():
    bot_token = 'your bot-token'
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(None, weather))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
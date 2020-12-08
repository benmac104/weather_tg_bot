import urllib
import urllib.request
from aiogram import Bot, Dispatcher, executor, types

import json

API_TOKEN = '1499275913:AAEOZP-jqwZkTr3WldgZIX43Noef7-D7IGs'

api_weather_adress = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=cc9e55c812f46c5ec09b695c9a39af80&units=metric&q="

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm WeatherBot!\nPowered by Ben Machlev.")


@dp.message_handler(commands=['play', 'new'])
async def send_start(message: types.Message):
    """
        This handler will be called when user sends `/play` or `/new` command
        """
    await message.reply("let's start!\nenter your city\n")


@dp.message_handler()
async def echo(message: types.Message):
    # get in open weather api and get json file
    # replay with the temp and description

    url_weather = api_weather_adress + message.text
    json_data = urllib.request.urlopen(url_weather)
    data = json.load(json_data)
    jtopy = json.dumps(data)
    dict_json = json.loads(jtopy)
    formatted_data = dict_json.get('list')
    temp = formatted_data[0]['main']['temp']
    await message.answer("now the temp is:" + str(temp))
    await message.answer("the sky is:" + formatted_data[0]['weather'][0]['description'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
import requests

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSdtH67ClEw3Jnu9U1PAeqTZZaWPY_On8BMZYIfexIi7Atn7LHyb1rMMg8LBmzgvEx3sALz3SL_vQQX/pub?gid=378550121&single=true&output=pdf"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

@dp.message_handler(Text(equals='EBITDA'))
async def command_ebitda(message: types.Message):
    client = requests.Session()
    response = client.get(url, headers=headers)

    FILE_TYPE = response.headers["content-type"].split("/")[1]

    with open(f"EBITDA.{FILE_TYPE}", "wb") as EBITDA:
        EBITDA.write(response.content)
    await bot.send_document(message.from_user.id, open('EBITDA.pdf', 'rb'))
    await message.delete()

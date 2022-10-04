from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

TOKEN = "5725016563:AAFMCtd6WGsKrbcrUwVwEyK_kW7fu96dIl4"

bot = Bot(token=TOKEN)

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["С пюрешкой","Без пюрешки"]
    keyboard.add(*buttons)
    await message.answer("Kaк подавать котлеты?",reply_markup=keyboard)
    

'''
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
'''

if __name__ == '__main__':
    executor.start_polling(dp)
#from aiogram.dispatcher.filters import Text
@dp.message_handler(Text(equals="С пюрешкой"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")



@dp.message_handler(lambda message: message.text == "Без пюрешки")
async def with_puree(message: types.Message):
    await message.reply("ЧЕЕЕЕЕЕЛ БОЖЕ  ЛИВНИ ОТСЮДА")

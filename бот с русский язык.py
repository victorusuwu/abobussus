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
    buttons = ["морфологический","морфемный","разбор существительного","разбор глагола","разбор прилагательного"]
    keyboard.add(*buttons)
    await message.answer("Выберете разбор слова который вас интересует:",reply_markup=keyboard)


'''
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
'''
@dp.message_handler(Text(equals="морфологический"))
async def with_puree(message: types.Message):
    await message.reply(" 1 Часть речи, общее значение. \n 2 Морфологические признаки. \n 2.1. Начальная форма слова. \n 2.2. Постоянные признаки. \n 2.3. Непостоянные признаки. \n 3. Синтаксическая роль в предложении.")



@dp.message_handler(lambda message: message.text == "морфемный")
async def with_puree(message: types.Message):
    await message.reply(" Разбор слова начинают с выполнять с выделения корня слова. Затем переходят к остальным морфемам: окончание, суффиксы, приставки, постфиксы. Не следует забывать про основу слова.")


@dp.message_handler(lambda message: message.text == "разбор глагола")
async def with_puree(message: types.Message):
    await message.reply("Инфинитив (начальная форма). \n Постоянные признаки:вид,переходность,возвратность,спряжение. \n Непостоянные признаки:наклонение глагола,время (для изъявительного наклонения),лицо (для настоящего, будущего времени и повелительного наклонения),число, род (для прошедшего времени и условного наклонения в единственном числе). \n Роль в предложении. ")

@dp.message_handler(commands="special_buttons")
async def  cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Запросить геолокацию",request_location=True))
    keyboard.add(types.KeyboardButton(text="Запросить контакт",request_contact=True))
    keyboard.add(types.KeyboardButton(text="Создать викторину",request_poll=types.KeyboardButtonPollType(type=types.QUIZ)))
    await message.answer("Выберете действие:",reply_markup=keyboard)
    
if __name__ == '__main__':
    executor.start_polling(dp)
#from aiogram.dispatcher.filters import Text

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import random

TOKEN = "5725016563:AAFMCtd6WGsKrbcrUwVwEyK_kW7fu96dIl4"

bot = Bot(token=TOKEN)

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["кринж","ботик","закибербулить ","забайтить ","закрысить ","леон"]
    keyboard.add(*buttons)
    await message.answer("Выберете современное слово которое вы хотите узнать:",reply_markup=keyboard)


'''
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
'''

@dp.message_handler(lambda message: message.text == "кринж")
async def with_puree(message: types.Message):
    await message.reply("жоское чувсво стыда при просмотре отборного ужаснейшего контента или любого видео в лайке")

@dp.message_handler(lambda message: message.text == "ботик")
async def with_puree(message: types.Message):
    await message.reply("называя человека или игрока ботиком обычно подразумевается его низкий скилл или же уровень игры и приводится сравнения с ботами в играх которые обычно очень слабы и тупы")


@dp.message_handler(lambda message: message.text == "закибербулить")
async def with_puree(message: types.Message):
    await message.reply("жестко унизить челвека через интернет но после появления мема ЧЕ ЗАКИБЕРБУЛИЛИ ТЕБЯ ДА? стал использоватся и в реальной жизни")


@dp.message_handler(lambda message: message.text == "забайтить")
async def with_puree(message: types.Message):
    await message.reply("забайтить означает обмануть врага или поймать его на ошибке ")
    
@dp.message_handler(lambda message: message.text == "закрысить")
async def with_puree(message: types.Message):
    await message.reply("грязный прием обычно применяемый игроками не имеющими особого скила означает неожиданную атаку из укрытия либо атака своего тиммейта ")

@dp.message_handler(lambda message: message.text == "леон")
async def with_puree(message: types.Message):
    await message.reply("ЭТО ЖЕ ЛЕООООООООООООООООООООООООООООН мечта всех школьников и тупая лягушка ради которой я играл в бравл старс 4 года")

@dp.message_handler(commands="special_buttons")
async def cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Запросить геолокацию", request_location=True))
    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
    keyboard.add(types.KeyboardButton(text="Создать викторину",
                                      request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(commands="inline_url")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)

@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(random.randint(1, 10)))
    
@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10)))
    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    # или просто await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp)
#from aiogram.dispatcher.filters import Text
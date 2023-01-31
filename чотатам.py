from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import random
from contextlib import suppress

TOKEN = "5671316973:AAFxAJI7gP4XILJ8kWxsNOKmAVrz6Y9UtMo"

bot = Bot(token=TOKEN)

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","список команд"]
    keyboard.add(*buttons)
    await message.answer("Выберете расписание на какой день вы хотите узнать:",reply_markup=keyboard)


'''
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
'''

@dp.message_handler(lambda message: message.text == "Понедельник")
async def with_puree(message: types.Message):
    await message.reply("1-Кл.час \n 2-Геогр \n 3-Русский \n 4-Русский \n 5-Обществознание ")

@dp.message_handler(lambda message: message.text == "Вторник")
async def with_puree(message: types.Message):
    await message.reply("1-Англ \n 2-Англ \n 3-Немиш \n 4-Физика \n 5-История \n 6-Геометрия")


@dp.message_handler(lambda message: message.text == "Среда")
async def with_puree(message: types.Message):
    await message.reply("1-Биология \n 2-Лит-ра \n 3-Алгебра \n 4-Алгебра \n 5-Физ-ра \n 6-История ")

@dp.message_handler(lambda message: message.text == "Четверг")
async def with_puree(message: types.Message):
    await message.reply("1-Геогр \n 2-Геометрия \n 3-Алгебра \n 4-Технология 5-Немиш 6-Русский")

@dp.message_handler(lambda message: message.text == "Пятница")
async def with_puree(message: types.Message):
    await message.reply("1-Лит-ра \n 2-ИЗО \n 3-Биология \n 4-Русский \n 5-Англ \n 6-Англ")

@dp.message_handler(lambda message: message.text == "Суббота")
async def with_puree(message: types.Message):
    await message.reply("1-Физ-ра \n 2-Физика \n 3-Инфор \n 4-Геом \n 5-Алгебра \n 6-Музыка")

@dp.message_handler(lambda message: message.text == "список команд")
async def with_puree(message: types.Message):
    await message.reply("/start /random /special_buttons /numbers")

@dp.message_handler(lambda message: message.text == "кринж")
async def with_puree(message: types.Message):
    await message.reply("жоское чувсво стыда при просмотре отборного ужаснейшего контента или любого видео в лайке")

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
user_data = {}

def get_keyboard():
    # Генерация клавиатуры.
    buttons = [
        types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="num_incr"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


    # Общая функция для обновления текста с отправкой той же клавиатуры
    async def update_num_text(message: types.Message, new_value: int):
        with suppress(MessageNotModified):
            await message.edit_text(f"Укажите число: {new_value}", reply_markup=get_keyboard())

@dp.message_handler(commands="numbers")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())

@dp.callback_query_handler(Text(startswith="num_"))
async def callbacks_num(call: types.CallbackQuery):
    # Получаем текущее значение для пользователя, либо считаем его равным 0
    user_value = user_data.get(call.from_user.id, 0)
    # Парсим строку и извлекаем действие, например `num_incr` -> `incr`
    action = call.data.split("_")[1]
    if action == "incr":
        user_data[call.from_user.id] = user_value+1
        await update_num_text(call.message, user_value+1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value-1
        await update_num_text(call.message, user_value-1)
    elif action == "finish":
        # Если бы мы не меняли сообщение, то можно было бы просто удалить клавиатуру
        # вызовом await call.message.delete_reply_markup().
        # Но т.к. мы редактируем сообщение и не отправляем новую клавиатуру, 
        # то она будет удалена и так.
        await call.message.edit_text(f"Итого: {user_value}")
    # Не забываем отчитаться о получении колбэка
    await call.answer()

    # Здесь хранятся пользовательские данные.
# Т.к. это словарь в памяти, то при перезапуске он очистится
user_data = {}

def get_keyboard():
    # Генерация клавиатуры.
    buttons = [
        types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="num_incr"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

async def update_num_text(message: types.Message, new_value: int):
    # Общая функция для обновления текста с отправкой той же клавиатуры
    await message.edit_text(f"Укажите число: {new_value}", reply_markup=get_keyboard())

@dp.message_handler(commands="numbers")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())

@dp.callback_query_handler(Text(startswith="num_"))
async def callbacks_num(call: types.CallbackQuery):
    # Получаем текущее значение для пользователя, либо считаем его равным 0
    user_value = user_data.get(call.from_user.id, 0)
    # Парсим строку и извлекаем действие, например `num_incr` -> `incr`
    action = call.data.split("_")[1]
    if action == "incr":
        user_data[call.from_user.id] = user_value+1
        await update_num_text(call.message, user_value+1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value-1
        await update_num_text(call.message, user_value-1)
    elif action == "finish":
        # Если бы мы не меняли сообщение, то можно было бы просто удалить клавиатуру
        # вызовом await call.message.delete_reply_markup().
        # Но т.к. мы редактируем сообщение и не отправляем новую клавиатуру, 
        # то она будет удалена и так.
        await call.message.edit_text(f"Итого: {user_value}")
    # Не забываем отчитаться о получении колбэка
    await call.answer()








if __name__ == '__main__':
    executor.start_polling(dp)
#from aiogram.dispatcher.filters import Text        
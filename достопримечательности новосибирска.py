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
    buttons = ["Новосибирский зоопарк имени Р.А. Шило","Новосибирский государственный академический театр оперы и балета","Аквапарк Аквамир","Большой новосибирский планетарий","Пятница","Суббота","список команд"]
    keyboard.add(*buttons)
    await message.answer("О какой достопримечательностиновосибирска вы хотите узнать?",reply_markup=keyboard)


'''
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
'''

@dp.message_handler(lambda message: message.text == "Новосибирский зоопарк имени Р.А. Шило")
async def with_puree(message: types.Message):
    await message.reply("Новосибирский зоопарк имени Ростислава Александровича Шило — один из крупнейших зоопарков России. Занимает площадь 65 га, в нём содержится около 11 000 особей 770 видов. Более 350 видов занесены в Международную красную книгу. Около 180 видов внесено в Красную книгу России и Региональные Красные Книги. На 110 видов ведутся международные племенные книги.")

@dp.message_handler(lambda message: message.text == "Новосибирский государственный академический театр оперы и балета")
async def with_puree(message: types.Message):
    await message.reply("Новосибирский театр оперы и балета – крупнейший музыкальный театр России. Коллектив театра зарекомендовал себя как один из лучших музыкально-театральных коллективов страны, что подтверждается участием в международных и российских фестивалях, множеством профессиональных наград и ярких постановок в репертуаре, обширной картой гастрольных туров. Здание Новосибирского театра оперы и балета по праву является символом и гордостью Сибирского региона.")


@dp.message_handler(lambda message: message.text == "Аквапарк Аквамир")
async def with_puree(message: types.Message):
    await message.reply("Аквапарк «Аквамир» в Новосибирске был открыт в 2016 году. Это один из самых новых и самый большой крытый аквапарк в России.«Аквамир» отличается от подобных аквапарков широким спектром услуг, многие из которых редкие или уникальные. Здесь есть необычные термы, водные горки и аттракционы, детская игровая зона, а также классические и известные многим развлечения. ")

@dp.message_handler(lambda message: message.text == "Большой новосибирский планетарий")
async def with_puree(message: types.Message):
    await message.reply("Крупнейший планетарий за уралом.В планетарии можно увидеть Полнокупольные программы,Обсерватории,Башня Фуко,и парк")

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
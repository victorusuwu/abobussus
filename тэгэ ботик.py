from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import link
import random
from contextlib import suppress

TOKEN = "6290945810:AAF54axaz05zqHF8V6fzWqI5iS3nwLzPW2s"

bot = Bot(token=TOKEN)

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["фота","Новосибирский зоопарк имени Р.А. Шило","Новосибирский государственный академический театр оперы и балета","Аквапарк Аквамир","Большой новосибирский планетарий","Центральный сибирский ботанический сад ","Музей железнодорожной техники ","Музей мировой погребальной культуры ","Собор святого благоверного князя Александра Невского ","Технопарк новосибирского Академгородка ","список команд"]
    keyboard.add(*buttons)
    await message.answer("О какой достопримечательности новосибирска вы хотите узнать?",reply_markup=keyboard)


'''
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
'''
#('<b>hello</b><a href="https://2gis.ru/novosibirsk/firm/141265769338187">2гис</a>',parse_mode='HTML')









@dp.message_handler(lambda message: message.text == "фота")
async def with_puree(message: types.Message):
    with open('diz.png', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

@dp.message_handler(lambda message: message.text == "Новосибирский зоопарк имени Р.А. Шило")
async def with_puree(message: types.Message):
    with open('diz.png', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)
    await message.reply("<b>Новосибирский зоопарк имени Ростислава Александровича Шило — один из крупнейших зоопарков России. Занимает площадь 65 га, в нём содержится около 11 000 особей 770 видов. Более 350 видов занесены в Международную красную книгу. Около 180 видов внесено в Красную книгу России и Региональные Красные Книги. На 110 видов ведутся международные племенные книги.</b> \n \n <a href='https://zoonovosib.ru'>сайт зоопарка</a> \n \n <a href='https://2gis.ru/novosibirsk/firm/141265769338187'>смотреть на картах</a>",parse_mode='HTML')

@dp.message_handler(lambda message: message.text == "Новосибирский государственный академический театр оперы и балета")
async def with_puree(message: types.Message):
    await message.reply("<b> Новосибирский театр оперы и балета – крупнейший музыкальный театр России. Коллектив театра зарекомендовал себя как один из лучших музыкально-театральных коллективов страны, что подтверждается участием в международных и российских фестивалях, множеством профессиональных наград и ярких постановок в репертуаре, обширной картой гастрольных туров. Здание Новосибирского театра оперы и балета по праву является символом и гордостью Сибирского региона.</b> \n <a href='https://novat.nsk.ru/'>сайт театра</a>",parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Аквапарк Аквамир")
async def with_puree(message: types.Message):
    await message.reply("Аквапарк «Аквамир» в Новосибирске был открыт в 2016 году. Это один из самых новых и самый большой крытый аквапарк в России.«Аквамир» отличается от подобных аквапарков широким спектром услуг, многие из которых редкие или уникальные. Здесь есть необычные термы, водные горки и аттракционы, детская игровая зона, а также классические и известные многим развлечения. ")

@dp.message_handler(lambda message: message.text == "Большой новосибирский планетарий")
async def with_puree(message: types.Message):
    await message.reply("Крупнейший планетарий за уралом.В планетарии можно увидеть Полнокупольные программы,Обсерватории,Башня Фуко,и парк")

@dp.message_handler(lambda message: message.text == "Центральный сибирский ботанический сад")
async def with_puree(message: types.Message):
    await message.reply("Центральный сибирский ботанический сад был организован в 1946 году по инициативе академика Владимира Леонтьевича Комарова. Ботанический сад располагается в непосредственной близости от Новосибирского Академгородка и занимает территорию площадью 850 га. По территории Ботсада протекает речка Зырянка, на которой расположен пруд. Ботанический сад имеет не только научное значение, но также является популярным местом отдыха для многих жителей Академгородка. В Ботсаду созданы крупнейшие в Азиатской России коллекции пищевых, лекарственных, пряно-ароматических, декоративных, редких и исчезающих растений; экспозиции «Парк Бонсай», «Вальс цветов», «Вересковый сад», «Дендрарий», «Регулярный французский сад», «Сад непрерывного цветения», «Сад топиарного искусства», «Лекарственные и пряно-ароматические растения», «Кактусы и другие суккуленты Старого и Нового света», «Растения тропических и субтропических областей Земного шара», «Экзотические овощные растения». В дендрарии на площади более 20 га собрано свыше 500 видов, гибридов и форм древесных растений различного географического происхождения. В оранжереях представлено более 7000 видов, форм и сортов тропических и субтропических растений из Европы, Азии, Африки и Америки, в том числе уникальные коллекции кактусов и суккулентов, папоротников, бегоний и ароидных.\nСайт https://csbg-nsk.ru/")

@dp.message_handler(lambda message: message.text == "Музей железнодорожной техники")
async def with_puree(message: types.Message):
    await message.reply("Музей железнодорожной техники был основан в 2000 году усилиями Западно-Сибирской железной дороги, ветеранов-работников железной дороги и Николая Архиповича Акулинина (заместителя начальника железной дороги). С весны 1998 года было собрано 63 экспоната. На его территории выставлены реальные составы и вагоны с середины XIX века и до наших дней. Причем посетители могут осмотреть железнодорожную технику не только снаружи, но и заглянуть в операционный вагон времен Великой Отечественной войны или побывать в императорском купе. Протяжённость выставочных площадок составляет около трёх километров. В музее собрана большая коллекция паровозов, тепловозов, электровозов, вагонов, в основном работавших на железных дорогах Западной Сибири. Кроме того, в коллекции музея имеются советские легковые автомобили ГАЗ, Москвич, ЗАЗ разных годов выпуска, а также несколько грузовиков, тракторов и вездеходов. ")



@dp.message_handler(lambda message: message.text == "Музей мировой погребальной культуры")
async def with_puree(message: types.Message):
    await message.reply("Музей мировой погребальной культуры посвящён похоронным традициям различных народов. Является единственным в России музеем данной направленности. Музей создан в 2012 г. президентом международной выставки «Некрополь», академиком Европейской академии естественных наук и вице-президентом Союза похоронных организаций и крематориев, предпринимателем С. Б. Якушиным. Основу коллекций музея составляют экспонаты XIX — начала XX веков. Всего музей содержит несколько десятков тысяч экспонатов, среди них около 200 траурных платьев XIX века, модели катафалков, около 10 000 гравюр похоронной тематики, около 1000 картин и скульптур, а также около 9000 фотографий и 11 000 открыток, присутствует ряд медальных экспонатов. В музее хранятся различные образцы официальных документов, заключений судебной экспертизы, листовки, некрологи, фирменные бланки, и т. п. Всего документальный фонд насчитывает около 6000 экспонатов. В музее имеются разделы посвящённые кладбищенской архитектуре, исследуются типологии намогильного креста и могильных плит XIX века. \n          Сайт https://musei-smerti.ru/ \n          Как добратьсяАвтобус	№ 203 от остановки «ПКиО «Березовая роща» до остановки «Новосибирский крематорий»Маршрутное такси	№ 399 от остановок «Площадь Калинина» (станция метро «Заельцовская») или «Сад Дзержинского» до остановки «Новосибирский крематорий».")

@dp.message_handler(lambda message: message.text == "Собор святого благоверного князя Александра Невского")
async def with_puree(message: types.Message):
    await message.reply("Собор святого благоверного князя Александра Невского — православный храм в Новосибирске, построенный как памятник устроителю Великого Сибирского пути императору Александру III. Одно из первых каменных зданий города. Решение о возведении Храма во имя Александра Невского приняли в 1895 году. К 1899 году каменный храм в неовизантийском стиле был закончен и освещен епископом Макарием. Статус собора Храм во имя Александра Невского получил в 1915 году. В 1937 году собор был закрыт. Предпринимались попытки взорвать здание, но были разрушены только перегородки. Движение за возвращение собора церкви развернулось в 1988 году, в год празднования 1000-летия Крещения Руси. Активное участие в нём принял митрополит Новосибирский и Барнаульский Гедеон (Докукин). В 1989 г. Новосибирский городской совет передал храм церкви. 15 мая 1991 года собор был освящён Патриархом Московским и всея Руси Алексием II. Сразу после передачи собора церкви начались восстановительные работы. Колокольня была вновь отстроена, купола храма перекрыты, обновлены поврежденные и пришедшие в негодность фрагменты внешних стен, восстановлена внутренняя планировка и заново отштукатурены внутренние стены храма. В 2017 г. у Южных врат Александро-Невского собора был открыт памятник Николаю II и цесаревичу Алексею. Высота фигуры Николая II составляет 3,6 метра, фигуры цесаревича — 2,7 метра. Открытие памятника было приурочено к 99-й годовщине расстрела царской семьи. \n          Сайт http://ansobor.ru \nКак добраться:\n Автобус	Ост. «Площадь Свердлова», №№ 8, 1113, 21, 1038, 1232, 1141, 54, 122\n Троллейбус	Ост. «Площадь Свердлова», №№ 13, 29 \n Маршрутное такси	Ост. «Площадь Свердлова», № 1")

@dp.message_handler(lambda message: message.text == "Технопарк новосибирского Академгородка")
async def with_puree(message: types.Message):
    await message.reply("Технопарк новосибирского Академгородка - комплексный научно-технологический парк, обладающий уникальной инновационной и деловой инфраструктурой. построен в 2013 г. Здание Технопарка состоит из двух секций, соединенных надземным коридором-переходом. Строение имеет необычную и довольно интересную архитектуру. \n    В настоящее время Технопарк ведет работу по 4 направлениям: информационные технологии, приборостроение, нанотехнологии и новые материалы, биотехнологии и биомедицина. Для каждого кластера создана технологическая инфраструктура, построены лабораторно-производственные и офисные здания, действуют бизнес-инкубаторы. \n        Сайт academpark.com \n Как добраться: \n Автобус 23,47,48,7,8 \n Маршрутка 52,7 \n Остановка общественного транспорта «Технопарк»")


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
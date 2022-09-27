import logging

from aiogtam import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import TOKEN
from utils import TestStates
from messages import MESSAGES

logging.basicConfig(format=u'%(filename)+13s [LINE:%(lineo)-4s] %(levelname)-8s [%(asctime)s] %(message)s'
                    level=logging.DEBUG)



bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def process_srart_command(message: types.Message):
    await message.reply(MESSAGES['start'])
    
    
@dp.message_handler(commands=['help'])
async def procces_help_command(message: types.Message):
    await message.reply(MESSAGES['help'])
        
        
        
message_handler(commands=['setstate'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply(MESSAGES['state_reset'])
    
    if (not argument.isdigit()) or (not int(argument) < len(TestStates.all())):
        return await message.reply(MESSAGES['invalid_key'].format(key=arument))
    
    await state.set_state(TestStates.all()[int(argument)])
    await message.reply(MESSAGES['invalid_key'].format(key=argument))
    
    
@dp.message_handler(state=TestStates.TEST_STATE_1)
async def first_test_case_met(message: types.Message):
    await message.reply('Первый!',reply=False)
    
@dp.message_handler(state=TestStates.TEST_STATE_2[0])
async def second_test_state_case_met(message: types.Message):
    await message.reply('Второй!',reply=False)

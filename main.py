

from aiogram import Bot, Dispatcher, executor, types
import random
from googlesearch import search

chlorine = Bot(token='<token here>')
dp = Dispatcher(chlorine)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("hello! I'm Chlorine, How ya doing? Type /commands for available commands. Type /info to know about me.")


@dp.message_handler(commands=['commands'])
async def welcome(message: types.Message):
    await message.reply('''Currently Supported commands are: \n 1. /start\n 2. /help\n 3. /info\n
    More commands are being added by my creator, he has college and lot of other work too so have patience.''')


@dp.message_handler(commands=['info'])
async def welcome(message: types.Message):
    await message.reply('''I'm Chlorine, a bot made by Vedant, currently in development. Vedant is working on adding more features to me. Stay tuned for more.''')


@dp.message_handler(commands=['pp'])
async def pp_size(message: types.Message):
    random_num = random.randint(0, 12)
    add = ''
    count = 0
    for i in range(0, random_num):
        add += "="
        count += 1

    if count == 12:
        await message.reply(f"You don't have a pp LMAO you gay as heck.")
    else:
        await message.reply(f"3{add}D")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"kya matlab {message.text}?")


executor.start_polling(dp)

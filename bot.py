from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic, code, pre

from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

import keyboards as kb

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    msg = text(bold('Hello, I am cryptobot, write coin symbol or:'),
               '/help', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Write coin symbol or:'),
               '/help', '/example', '/group', '/all', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['example'])
async def process_help_command(message: types.Message):
    msg = text(('Example:\n'), bold('BTC'), '\nBitcoin (BTC) is a cryptocurrency\nBitcoin is 48,086.15609069 USD'
                                            '\nBTC is down -0.04 over the last 24 hours.')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['BTC'])
async def btc_command(message: types.Message):
    await message.reply("BTC", reply_markup=kb.markup_all)


@dp.message_handler(commands=['ETH'])
async def eth_command(message: types.Message):
    await message.reply("ETH", reply_markup=kb.markup_all)


@dp.message_handler(commands=['TON'])
async def ton_command(message: types.Message):
    await message.reply("TON", reply_markup=kb.markup_all)


@dp.message_handler(commands=['I'])
async def sol_command(message: types.Message):
    await message.reply("You?", reply_markup=kb.markup_request)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    msg = text(('Я не знаю такой команды\nПопробуй, использовать, команду'), code('/help'))
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

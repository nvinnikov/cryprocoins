from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nIt is cryptobot, write coin symbol or --h/help")

@dp.message_handler(commands=['help', '--h'])
async def process_help_command(message: types.Message):
    await message.reply('Write coin symbol or:\n(--h) - help\n(--q) - quit\n(--x) - example\n(--a) - all coins')

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)


# while True:
#     x = input()
#     qq = Cryptocurrency()
#     all = qq.get_all_symbols()
#     if x == '--h':
#         print('Write coin symbol or:\n(--h) - help\n(--q) - quit\n(--x) - example\n(--a) - all coins')
#         continue
#     if x == '--x':
#         print(qq.get_20_coins())
#         print('Example:\nBTC\nBitcoin (BTC) is a cryptocurrency\nBitcoin is 48,086.15609069 USD\nBTC is down -0.04 over the last 24 hours.')
#     if x == '--a':
#         print(all)
#     if x in all:
#         print(qq.get_coin_description_by_symbol(x))
#         print(qq.get_market_price(x))
#         print(qq.get_market_statistic(x))
#         continue
#     if x == '--q':
#         exit()
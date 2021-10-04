from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_btc = KeyboardButton('/BTC')
button_eth = KeyboardButton('/ETH')
button_ton = KeyboardButton('/TON')

markup3 = ReplyKeyboardMarkup().add(
    button_btc).add(button_eth).add(button_ton)

markup4 = ReplyKeyboardMarkup().row(
    button_btc, button_eth, button_ton
)

markup_all = ReplyKeyboardMarkup().row(
    button_btc, button_eth, button_ton
).add(KeyboardButton('ALL'))


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)
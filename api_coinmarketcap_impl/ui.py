from quotes import MarketFeel
from cryptocurrency import Cryptocurrency

today = MarketFeel()
print('Hello, today markets are ' + today.market_status() + ', so:' + '\n' + today.fells())
print('Do you want to know something about crypto? Write coin symbol or help (--h).')


while True:
    x = input()
    qq = Cryptocurrency()
    all = qq.get_all_symbols()
    if x == '--h':
        print('Write coin symbol or:' + '\n' + '(--h) - help' +'\n' + '(--q) - quit' + '\n' + '(--x) - example' + '\n' + '(--a) - all coins')
        continue
    if x == '--x':
        print(qq.get_20_coins())
        print('Example:' + '\n' + 'BTC' + '\n' + "Bitcoin (BTC) is a cryptocurrency" + '\n' +
              "Bitcoin is 48,086.15609069 USD" + '\n' + "BTC is down -0.04 over the last 24 hours.")
    if x == '--a':
        print(all)
    if x in all:
        print(qq.get_coin_description_by_symbol(x))
        print(qq.get_market_price(x))
        print(qq.get_market_statistic(x))
        continue
    if x == '--q':
        exit()
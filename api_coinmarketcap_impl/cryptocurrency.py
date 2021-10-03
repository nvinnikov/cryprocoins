import requests
from const import u_token, headers, base_url, cryptocurrency_url
from connect import _expt


class Cryptocurrency(object):
    def __init__(self, symbol=None, coin_id=None):
        self.symbol = symbol
        self.coin_id = coin_id

    def _get_map(self):
        _url = 'map'
        url = base_url + cryptocurrency_url + _url
        response = requests.get(url, headers=headers)
        mp = _expt(response)
        return mp['data']

    def get_20_coins(self):
        mp = self._get_map()
        coins_map = []
        for i in mp:
            idd = []
            symbol = i['symbol']
            name = i['name']
            idd.append(name), idd.append(symbol)
            coins_map.append(idd)
            if len(coins_map) > 20:
                return coins_map
        return coins_map

    def _get_info_by_symbol(self, symbol):
        _url = 'info?symbol='
        url = base_url + cryptocurrency_url + _url + symbol
        response = requests.get(url, headers=headers)
        mp = _expt(response)
        return mp['data']

    def _get_info_by_coin_id(self, coin_id):
        _url = 'info?id='
        url = base_url + cryptocurrency_url + _url + str(coin_id)
        response = requests.get(url, headers=headers)
        mp = _expt(response)
        return mp['data']

    def get_symbol_id(self, symbol):
        mp = self._get_info_by_symbol(symbol)
        return mp[symbol]['id']

    def get_coin_description_by_symbol(self, symbol):
        mp = self._get_info_by_symbol(symbol)
        return mp[symbol]['description']

    def get_coin_description_by_id(self, coin_id):
        mp = self._get_info_by_coin_id(coin_id)
        return mp[coin_id]['description']

    def get_all_symbols(self):
        all = []
        mp = self._get_map()
        for i in mp:
            ii = i['symbol']
            all.append(ii)
        return all

    def get_market_price(self, symbol):
        string = self.get_coin_description_by_symbol(symbol)
        f = string.find('known price of') + 15 #151+15
        l = string.find('USD and is') + 3 #193+3
        return string[f:l]

    def get_market_statistic(self, symbol):
        string = self.get_coin_description_by_symbol(symbol)
        f = string.find(' USD and is ') + 9
        l = string.find(' It is currently trading')
        return(symbol + ' ' + string[f:l])

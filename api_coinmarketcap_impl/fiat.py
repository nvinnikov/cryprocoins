import requests
from const import u_token, headers, base_url, cryptocurrency_url, FIAT_SYMBOL_ID
from connect import _expt


class Fiat(object):
    def __init__(self, symbol=None, fiat_id=None):
        self.symbol = symbol
        self.fiat_id = fiat_id

    def _get_fiat_map(self):
        _url = 'fiat/map'
        url = base_url + _url
        response = requests.get(url, headers=headers)
        mp = _expt(response)
        return mp['data']

    def _get_fiat_by_symbol(self, symbol):
        mp = self._get_fiat_map()
        for i in mp:
            if symbol == i['symbol']:
                fiat_info = i
                return fiat_info
            else:
                fiat_info = None
        return fiat_info

    def _get_fiat_by_id(self, fiat_id):
        mp = self._get_fiat_map()
        for i in mp:
            if fiat_id == i['id']:
                fiat_info = i
                return fiat_info
            else:
                fiat_info = None
        return fiat_info

    def get_fiat_by_symbol(self, symbol):
        fiat_info = self._get_fiat_by_symbol(symbol)
        if fiat_info is not None:
            return str(fiat_info['sign']) + ' ' + str(fiat_info['symbol']) + ' ' + str(fiat_info['name'])
        else:
            return None

    def get_fiat_by_id(self, fiat_id):
        fiat_info = self._get_fiat_by_id(fiat_id)
        if fiat_info is not None:
            return str(fiat_info['sign']) + ' ' + str(fiat_info['symbol']) + ' ' + str(fiat_info['name'])
        else:
            return None

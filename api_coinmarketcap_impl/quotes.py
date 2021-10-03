import requests
from const import base_url, quotes_url, lates_url, headers
from connect import _expt


class Quotes(object):
    def __init__(self):
        pass

    def _quotes_info_latest(self):
        url = base_url + quotes_url + lates_url
        response = requests.get(url, headers=headers)
        mp = _expt(response)
        return mp['data']

    def btc_dominance_today(self):
        return str(self._quotes_info_latest()['btc_dominance'])

    def btc_dominance_yesterday(self):
        return str(self._quotes_info_latest()['btc_dominance_yesterday'])

    def btc_dominance_24h_percentage_change(self):
        return str(self._quotes_info_latest()['btc_dominance_24h_percentage_change'])

    def eth_dominance_today(self):
        return str(self._quotes_info_latest()['eth_dominance'])

    def eth_dominance_yesterday(self):
        return str(self._quotes_info_latest()['eth_dominance_yesterday'])

    def eth_dominance_24h_percentage_change(self):
        return str(self._quotes_info_latest()['eth_dominance_24h_percentage_change'])

    def total_cryptocurrencies(self):
        return str(self._quotes_info_latest()['total_cryptocurrencies'])

    def active_market_pairs(self):
        return str(self._quotes_info_latest()['active_market_pairs'])


class MarketFeel:
    def __init__(self):
        self.q = Quotes()

    def fells(self):
        return ('BTC dominance today ' + self.q.btc_dominance_today() + '%, 24 hours change ' +
                self.q.btc_dominance_24h_percentage_change() + '%' + '\n' +
                'ETH dominance today ' + self.q.eth_dominance_today() + '%, 24 hours change ' +
                self.q.eth_dominance_24h_percentage_change() + '%' + '\n' +
                'Active ' + self.q.active_market_pairs() + ' pairs' + '\n' +
                'Total cryptocoins ' + self.q.total_cryptocurrencies() + '\n')

    def market_status(self):
        if float(self.q.btc_dominance_24h_percentage_change()) >= 0:
            return 'up'
        else:
            return 'down'



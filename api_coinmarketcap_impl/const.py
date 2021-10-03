OK = 'Connection Available'
BAD = 'Connection Refused'
TWO = 2
FIVE = 5

u_token = 'dc8e7015-2833-4358-8c86-68e5de56040c'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': u_token,
}

base_url = 'https://pro-api.coinmarketcap.com/v1/'
try_url = 'https://coinmarketcap.com'
cryptocurrency_url = 'cryptocurrency/'
quotes_url = 'global-metrics/quotes/'
lates_url = 'latest'

FIAT_SYMBOL_ID = {"USD": 2781, "ALL": 3526, "DZD": 3537, "ARS": 2821, "MD": 3527, "AUD": 2782, "AZN": 3528, "BHD": 3531,
                  "BDT": 3530, "BYN": 3533, "BMD": 3532, "BOB": 2832, "BAM": 3529, "BRL": 2783, "BGN": 2814, "EGP": 3538,
                  "EUR": 2790, "GEL": 3539, "GHS": 3540, "JPY": 2797, "JOD": 3546, "KZT": 3551, "KES": 3547, "KWD": 3550,
                  "KGS": 3548, "LBP": 3552, "MKD": 3556, "MUR": 2816, "MXN": 2799, "MDL": 3555, "MNT": 3558,"MAD": 3554,
                  "GBP": 2791, "RUB": 2806, "SGD": 2808, "ZAR": 2812, "TRY": 2810, "UAH": 2824, "AED": 2813}

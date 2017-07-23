import yql
import json
import os
import time
import datetime
import cryptowatch as cpt
import viabtc as via
import bitfinex as finex
import bitflyer as bf
import okcoin_usd as ok_usd
import okcoin_cny as ok_cny

time = int(time.mktime(datetime.datetime.now().timetuple()))
usdjpy = yql.getUSDJPY()
cnyjpy = yql.getCNYJPY()
btcusd_bitfinex = finex.getPrice("btcusd")
btcusd_okcoin_usd = ok_usd.getPrice("btc_usd")
btccny_okcoin_cny = ok_cny.getPrice("btc_cny")
btcjpy_bitflyer = bf.getPrice("BTC_JPY")
btcfxjpy = bf.getPrice("FX_BTC_JPY")
bcccny = via.getPrice("bcccny")

data = {
        "Time": time,
        "USDJPY": usdjpy,
        "CNYJPY": cnyjpy,
        "BTCUSD": {
            "Bitfinex": btcusd_bitfinex,
            "OKCoin": btcusd_okcoin_usd
            },
        "BTCCNY": {
            "OKCoin": btccny_okcoin_cny
            },
        "BTCJPY": {
            "Bitflyer": btcjpy_bitflyer
            },
        "BTCFXJPY": {
            "Bitflyer": btcfxjpy
            },
        "BCCCNY": {
            "ViaBTC": bcccny
            }
        }

path = os.path.abspath(os.path.dirname(__file__))
try:
    f = open(path + '/.data', 'w')
except:
    pass
else:
    f.write(json.dumps(data))
    f.close()

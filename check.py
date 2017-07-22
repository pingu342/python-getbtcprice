import yql
import json
import os
import time
import datetime
import cryptowatch as cpt
import viabtc as via
import bitfinex as finex
import bitflyer as bf

time = int(time.mktime(datetime.datetime.now().timetuple()))
usdjpy = yql.getUSDJPY()
cnyjpy = yql.getCNYJPY()
btcusd = finex.getPrice("btcusd")
btcjpy = bf.getPrice("BTC_JPY")
btcfxjpy = bf.getPrice("FX_BTC_JPY")
bcccny = via.getPrice("bcccny")

data = {
        "Time": time,
        "USDJPY": usdjpy,
        "CNYJPY": cnyjpy,
        "BTCUSD": {
            "Bitfinex": btcusd
            },
        "BTCJPY": {
            "Bitflyer": btcjpy
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

import json
import sys
import os
import time
import datetime

path = os.path.abspath(os.path.dirname(__file__))
try:
    f = open(path + '/.data', 'r')
except:
    print "no data"
    sys.exit()
else:
    data = json.load(f)
    f.close()

usdjpy = data["USDJPY"]
cnyjpy = data["CNYJPY"]
btcusd_bitfinex = data["BTCUSD"]["Bitfinex"]
btcusd_okcoin_usd = data["BTCUSD"]["OKCoin"]
btccny_okcoin_cny = data["BTCCNY"]["OKCoin"]
btcjpy_bitflyer = data["BTCJPY"]["Bitflyer"]
btcjpy_bitfinex = btcusd_bitfinex * usdjpy
btcjpy_okcoin_usd = btcusd_okcoin_usd * usdjpy
btcjpy_okcoin_cny = btccny_okcoin_cny * cnyjpy
btcfxjpy = data["BTCFXJPY"]["Bitflyer"]
bcccny = data["BCCCNY"]["ViaBTC"]
t = int(time.mktime(datetime.datetime.now().timetuple())) - data["Time"]
if (t < 60):
    print "  *** %2ds ago ***" % (t)
else:
    print "*** %2dm%2ds ago ***" % (t/60, t%60)
print "USDJPY    : %.2f" % (usdjpy)
print "CNYJPY    : %.2f" % (cnyjpy)
print "BTCUSD"
print " Bitfinex : %.1f" % (btcusd_bitfinex)
print " OKCoinUS : %.1f" % (btcusd_okcoin_usd)
print "BTCCNY"
print " OKCoinCN : %.1f" % (btccny_okcoin_cny)
print "BTCJPY"
print " Bitflyer : %.1f" % (btcjpy_bitflyer)
print " --- "
print " Bitfinex : %.1f" % (btcjpy_bitfinex)
print "     Diff : %+.1f" % -(btcjpy_bitflyer - btcjpy_bitfinex)
print " OKCoinUS : %.1f" % (btcjpy_okcoin_usd)
print "     Diff : %+.1f" % -(btcjpy_bitflyer - btcjpy_okcoin_usd)
print " OKCoinCN : %.1f" % (btcjpy_okcoin_cny)
print "     Diff : %+.1f" % -(btcjpy_bitflyer - btcjpy_okcoin_cny)
print "BTCFXJPY"
print " Bitflyer : %.1f" % (btcfxjpy)
print "BCCCNY"
print " ViaBTC   : %.1f" % (bcccny)
print "BCCJPY"
print " ViaBTC   : %.1f" % (bcccny * cnyjpy)


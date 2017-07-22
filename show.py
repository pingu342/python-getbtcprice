import json
import sys
import os
import time
import datetime

path = os.path.abspath(os.path.dirname(__file__))
try:
    f = open(path + '/.data', 'r')
except:
    sys.exit()
else:
    data = json.load(f)
    f.close()

t = data["Time"]
usdjpy = data["USDJPY"]
cnyjpy = data["CNYJPY"]
btcusd = data["BTCUSD"]["Bitfinex"]
btcjpy = data["BTCJPY"]["Bitflyer"]
btcfxjpy = data["BTCFXJPY"]["Bitflyer"]
bcccny = data["BCCCNY"]["ViaBTC"]

t = int(time.mktime(datetime.datetime.now().timetuple())) - t

print "*** %d second ago ***" % (t)
print "USDJPY    : %.2f" % (usdjpy)
print "CNYJPY    : %.2f" % (cnyjpy)
print "BTCUSD"
print " Bitfinex : %.1f" % (btcusd)
print "BTCJPY"
print " Bitfinex : %.1f" % (btcusd * usdjpy)
print " Bitflyer : %.1f" % (btcjpy)
print " (Diff    : %.1f)" % (btcjpy - btcusd*usdjpy)
print "BTCFXJPY"
print " Bitflyer : %.1f" % (btcfxjpy)
print "BCCCNY"
print " ViaBTC   : %.1f" % (bcccny)
print "BCCJPY"
print " ViaBTC   : %.1f" % (bcccny * cnyjpy)


import yql
import cryptowatch as cpt
import viabtc as via
import bitfinex as finex
import bitflyer as bf

usdjpy = yql.getUSDJPY()
print "USDJPY    : %.2f" % (usdjpy)

cnyjpy = yql.getCNYJPY()
print "CNYJPY    : %.2f" % (cnyjpy)

#btcusd = cpt.getPrice("bitfinex", "btcusd");
btcusd = finex.getPrice("btcusd");
print "BTCUSD"
print " Bitfinex : %.1f" % (btcusd)

#btcjpy = cpt.getPrice("bitflyer", "btcjpy");
btcjpy = bf.getPrice("BTC_JPY");
print "BTCJPY"
print " Bitfinex : %.1f" % (btcusd * usdjpy)
print " Bitflyer : %.1f" % (btcjpy)
print " (Diff    : %.1f)" % (btcjpy - btcusd*usdjpy)

#btcfxjpy = cpt.getPrice("bitflyer", "btcfxjpy");
btcfxjpy = bf.getPrice("FX_BTC_JPY");
print "BTCFXJPY"
print " Bitflyer : %.1f" % (btcfxjpy)

bcccny = via.getPrice("bcccny")
print "BCCCNY"
print " ViaBTC   : %.1f" % (bcccny)
print "BCCJPY"
print " ViaBTC   : %.1f" % (bcccny * cnyjpy)

#allowance = cpt.loadAllowance()
#remain = float(allowance["remaining"]) / 1000000000.0
#print "---"
#print "cryptowatch %.3f sec" % remain

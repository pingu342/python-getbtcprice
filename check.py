import yql
import cryptowatch as cpt
import viabtc as via

usdjpy = yql.getUSDJPY()
print "USDJPY    : %.2f" % (usdjpy)

cnyjpy = yql.getCNYJPY()
print "CNYJPY    : %.2f" % (cnyjpy)

btcusd = cpt.getPrice("bitfinex", "btcusd");
print "BTCUSD"
print " Bitfinex : %.1f" % (btcusd)

btcjpy = cpt.getPrice("bitflyer", "btcjpy");
print "BTCJPY"
print " Bitfinex : %.1f" % (btcusd * usdjpy)
print " Bitflyer : %.1f" % (btcjpy)
print " (Diff    : %.1f)" % (btcjpy - btcusd*usdjpy)

btcfxjpy = cpt.getPrice("bitflyer", "btcfxjpy");
print "BTCFXJPY"
print " Bitflyer : %.1f" % (btcfxjpy)

bcccny = via.getPrice("bcccny")
print "BCCCNY"
print " ViaBTC   : %.1f" % (bcccny)
print "BCCJPY"
print " ViaBTC   : %.1f" % (bcccny * cnyjpy)

allowance = cpt.loadAllowance()
remain = float(allowance["remaining"]) / 1000000000.0
print "---"
print "cryptowatch %.3f sec" % remain

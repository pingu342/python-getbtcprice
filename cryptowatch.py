import urllib
import json
import ssl
import os
from pprint import pprint

ssl._create_default_https_context = ssl._create_unverified_context

path = os.path.abspath(os.path.dirname(__file__))

def saveAllowance(allowance):
    try:
        f = open(path + '/.allowance', 'w')
    except:
        pass
    else:
        f.write(json.dumps(allowance))
        f.close()

def loadAllowance():
    try:
        f = open(path + '/.allowance', 'r')
    except:
        allowance = {
            "cost": 100,
            "remaining": 2000000000
            }
    else:
        allowance = json.load(f)
        f.close()
    return allowance

def printMarkets():
    url = "https://api.cryptowat.ch/markets"
    res = urllib.urlopen(url)
    result = json.loads(res.read().decode('utf-8'))
    pprint(result)

def getPrice(market, currency):
    url = "https://api.cryptowat.ch/markets/" + market + "/" + currency + "/price"
    res = urllib.urlopen(url)
    result = json.loads(res.read().decode('utf-8'))
    saveAllowance(result["allowance"])
    return float(result["result"]["price"])


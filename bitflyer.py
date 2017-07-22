import urllib
import json
import ssl
import os
from pprint import pprint

ssl._create_default_https_context = ssl._create_unverified_context

def getPrice(market):
    url = "https://api.bitflyer.jp/v1/ticker?product_code=" + market
    res = urllib.urlopen(url)
    result = json.loads(res.read().decode('utf-8'))
    return float(result["ltp"])


import urllib
import json
import ssl
from pprint import pprint

ssl._create_default_https_context = ssl._create_unverified_context

def getPrice(pair):
    url = "https://query.yahooapis.com/v1/public/yql"
    q = 'select * from yahoo.finance.xchange where pair in ("' + pair + '")'
    params = {
            "q": q,
            "format": "json",
            "env": "store://datatables.org/alltableswithkeys"
            }
    url += "?" + urllib.urlencode(params)
    res = urllib.urlopen(url)

    result = json.loads(res.read().decode('utf-8'))
    #pprint(result)

    return float(result["query"]["results"]["rate"]["Rate"])


def getUSDJPY():
    return getPrice("USDJPY")

def getCNYJPY():
    return getPrice("CNYJPY")

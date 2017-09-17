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

    try:
        res = urllib.urlopen(url, timeout=5)
        result = json.loads(res.read().decode('utf-8'))
        #pprint(result)
        return float(result["query"]["results"]["rate"]["Rate"])
    except Exception as e:
        pass

    return 0.0

def getUSDJPY():
    return getPrice("USDJPY")

def getCNYJPY():
    return getPrice("CNYJPY")

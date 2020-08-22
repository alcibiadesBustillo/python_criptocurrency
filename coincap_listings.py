from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
currency = 'JPY'

parameters = {
  'start':'1',
  'limit':'10',
  'convert': currency,  
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    results = response.json()
#   data = json.dumps(results, sort_keys=True, indent=4)
#   print(data)
    data = results['data']
    for currency in data:
        id = currency['id']
        name = currency['name']
        symbol = currency['symbol']
        print("{}: {} ({})".format(id, name, symbol))

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
currency = 'JPY'

parameters = {
#   'start':'1',
#   'limit':'1',
  'convert': currency
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'd55f1816-3eff-4898-8df3-683159e4f8fb',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  results = response.json()
#   data = json.dumps(results, sort_keys=True, indent=4)
#   print(data)

  active_cryptocurrencies = results['data']['active_cryptocurrencies']
  active_market_pairs = results['data']['active_market_pairs']
  last_updated = results['data']['last_updated']
  total_market_cap = results['data']['quote'][currency]['total_market_cap']  
  total_volume_24h = results['data']['quote'][currency]['total_volume_24h']
  #total_cryptocurrencies = results['data']['total_cryptocurrencies']
  

  print("There are currently {} active cryptocurrencies and {} active pairs markets.".format(active_cryptocurrencies, active_market_pairs))
  print("The global cap of all cryptos is {} and the 24th global volume is {}".format(total_market_cap, total_volume_24h))
  print()
  print("This information was last updated on {}".format(last_updated))

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
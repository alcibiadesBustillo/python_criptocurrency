from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'apikeyy', # change this with the api key
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  results = response.json()
  data = json.dumps(results, sort_keys=True, indent=4)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
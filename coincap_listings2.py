from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


start = 1
limit =  100
convert = 'USD'
sort = 'id'

choice =  input("Do you want to enter any custom parameters? (y/n) ")
if choice == 'y':
    limit = input("What is the custom limit?: ")
    start = input("What is the custom start number?: ")
    sort = input("What do you want to sort by?: ")
    convert = input("What is your local currency?: ")

parameters = {
  'start':start,
  'limit':limit,
  'sort': sort,
  'convert': convert,  
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
    data = json.dumps(results, sort_keys=True, indent=4)
    print(data)
    

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
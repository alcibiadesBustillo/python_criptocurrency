from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


start = 1
limit =  100
convert = 'USD'
sort = 'price'

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
    #data = json.dumps(results, sort_keys=True, indent=4)
    #print(data)

    data = results['data']

    print()
    for currency in data:
      cmc_rank = currency['cmc_rank']
      name = currency['name']
      sysmbol = currency['symbol']
      circulating_supply = currency['circulating_supply']
      total_supply = currency['total_supply']
      quote = currency['quote'][convert]
      
      market_cap = quote['market_cap'] 
      hour_change = quote['percent_change_1h'] 
      day_change = quote['percent_change_24h'] 
      week_change = quote['percent_change_7d'] 
      price = quote['price'] 
      volume = quote['volume_24h']

      print("{}: {} ({})".format(cmc_rank, name, sysmbol)) 
      print("Market cap: \t\t${}".format(market_cap))
      print("Price: \t\t\t${}".format(price))
      print("24h Volume: \t\t{}".format(volume))
      print("Hour change: \t\t{}%".format(hour_change))
      print("Day change: \t\t{}%".format(day_change))
      print("Week change: \t\t{}%".format(week_change))      
      print("Total supply: \t\t{}".format(total_supply))
      print("Circulating supply: \t{}".format(circulating_supply))
      
      #print("Percentage of coins in circulation: {}".format(percentage))
      print()


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
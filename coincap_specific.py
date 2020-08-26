from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def setUp(url):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '',
    }
    
    session = Session()
    session.headers.update(headers)
    return session

def getTickerUrl(start=1, limit=100, convert='USD'):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'    

    parameters = {
    'start':start,
    'limit':limit,
    'convert': convert,  
    }

    session = setUp(url)

    try:
        response = session.get(url, params=parameters)
        results = response.json()

        data = results['data']
        ticker_url_pairs = {}
        for currency in data:
            #name = currency['name']
            id = currency['id']        
            symbol = currency['symbol']
            ticker_url_pairs[symbol] = id       

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    
    return ticker_url_pairs

def printData(currency, id):
    #print(currency[id])
    cmc_rank = currency[id]['cmc_rank']
    name = currency[id]['name']
    sysmbol = currency[id]['symbol']
    circulating_supply = currency[id]['circulating_supply']
    total_supply = currency[id]['total_supply']
    quote = currency[id]['quote']["USD"]
    
    market_cap = quote['market_cap'] 
    hour_change = quote['percent_change_1h'] 
    day_change = quote['percent_change_24h'] 
    week_change = quote['percent_change_7d'] 
    price = quote['price'] 
    volume = quote['volume_24h']

    print("{}: {} ({})".format(cmc_rank, name, sysmbol)) 
    print("Market cap: \t\t${}".format(market_cap))
    print("Price: \t\t\t${:,}".format(price))
    print("24h Volume: \t\t{}".format(volume))
    print("Hour change: \t\t{}%".format(hour_change))
    print("Day change: \t\t{}%".format(day_change))
    print("Week change: \t\t{}%".format(week_change))      
    print("Total supply: \t\t{}".format(total_supply))
    print("Circulating supply: \t{}".format(circulating_supply))
    
    #print("Percentage of coins in circulation: {}".format(percentage))
    print()
    

t_url = getTickerUrl()

while True:
    choice = input("Enter the ticker symbol of a cryptocurrency: ")
    choice = choice.upper()

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'    
    convert = 'USD'

    parameters = {
    'id':t_url[choice],    
    'convert': convert,  
    }

    session = setUp(url)
    try:
        response = session.get(url, params=parameters)
        results = response.json()

        data = json.dumps(results, sort_keys=True, indent=4)
        #print(data)
        data = results['data']
        printData(data, str(t_url[choice]))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    
    

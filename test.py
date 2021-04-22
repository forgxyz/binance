import json

# this imports python-binance into the python script
# if you get an error, make sure you installed it via pip install python-binance ... if on mac it's pip3 install python-binance
from binance.client import Client

"""
https://medium.com/@80draperj/introduction-to-binance-with-python-part-1-getting-started-7ed223a5643b
"""

# load api keys from local file
with open("credentials.json", "r") as f:
    creds = json.load(f)

# initialize an instance of the Client class using api keys
client = Client(creds['API_KEY'], creds['SECRET_KEY'])

# pull available tickers from binance
# tickers = client.get_all_tickers()

# print first 5 key-value pairs
# print(tickers[:5])

# trades = client.get_recent_trades(symbol='BNBBTC')
#
# print(trades[:5])

avg_price = client.get_avg_price(symbol='BNBBTC')
print(avg_price)

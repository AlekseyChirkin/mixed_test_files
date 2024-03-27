import requests
import json

url = 'https://api.binance.com/api/v3/trades'

response = requests.get(url, params={'symbol': 'BTCUSDT'})

trades = response.json()
for i in trades:
    print(i)

print(trades)
print(type(trades))

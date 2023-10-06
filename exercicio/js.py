import requests

r = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(r)
print(r.json())

dic_r = r.json()
print(dic_r['USDBRL']['bid'])

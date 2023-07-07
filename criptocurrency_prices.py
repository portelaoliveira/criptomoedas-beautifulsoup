from bs4 import BeautifulSoup
import requests
import re

link = 'https://coinmarketcap.com/'
req = requests.get(link)
site = BeautifulSoup(req.text, "html.parser")

tbody = site.find('tbody')
lines = tbody.find_all('tr')

moedas = {}

for line in lines:
    try:
        name = line.find(class_="kKpPOn").text
        code = line.find(class_="coin-item-symbol").text
        values = line.find_all(string=re.compile("\$"))
        price = values[0]
        percent = line.find_all(string=re.compile("%"))
        
        for i, perc in enumerate(percent):
            if "bQjSqS" in perc.parent["class"]:
                percent[i] = "-" + str(perc)

        var_1h = percent[0]
        var_24h = percent[1]
        var_7d = percent[2]
        
        market_cap = values[2]
        volume = values[3]
        dic = {"name": name, "code": code, "price": price, "market_cap": market_cap, "volume": volume,
              "var_1h": var_1h, "var_24h": var_24h, "var_7d": var_7d}
        moedas[name] = dic
    except AttributeError:
        break
print(moedas)

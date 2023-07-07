from bs4 import BeautifulSoup
import requests

link = 'https://coinmarketcap.com/'
req = requests.get(link)
site = BeautifulSoup(req.text, "html.parser")

tbody = site.find('tbody')
lines = tbody.find_all('tr')

for line in lines:
    text_line = line.get_text(separator=";")
    list_text = text_line.split(";")
    name = list_text[1]
    price = list_text[3]
    print(name, price)

"""
Получить названия наборов Warhammer 40000 с сайта https://hobbygames.ru/warhammer-40000

1. Отправить запрос на сайт и получить 200 response
2. Преобразовать полученный код в более читабельный вид
3. Вычленить информацию о названиях наборов
"""

import requests
from bs4 import BeautifulSoup
response_wh = requests.get("https://hobbygames.ru/warhammer-40000")

soup = BeautifulSoup(response_wh.text, "html.parser")
names = soup.findAll('a', class_='name')

for name in names:
    title = str(name)
    begin = title.find('title') + 7
    end = title.rfind('"')
    print(title[begin:end])

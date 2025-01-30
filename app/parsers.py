import asyncio
import aiohttp
import requests

from aiohttp.abc import BaseRequest
from bs4 import BeautifulSoup
import lxml
from lxml.html.diff import href_token

#from app.handlers import castle

URL_CASTLES = 'https://motr-online.com/tops/castles'

GUILDNAME = 'Дерзкий поринг'





async def parse_castles():
    ''' Парсинг данных с сайта, преобразование в словарь '''

    castles = []
    lst = []
    try:
        src = requests.get(URL_CASTLES)
    except:
        return 'Bad Request'

    soup = BeautifulSoup(src.text, 'lxml').findAll('a', class_= 'alllink')
    for i in soup:
        lst.append(i.text)

    data = {lst[i]: lst[i+1] for i in range(0, len(lst), 2)}

    if GUILDNAME not in data.values():
        return 'Вы сегодня без замков'
    for k, v in data.items():
        if v == GUILDNAME:
            castles.append(k)
    return castles

if __name__ == '__main__':
    a = asyncio.run(parse_castles())



"""
#попытка переделать в асинхрон

async def parse_castles():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_CASTLES) as response:
            src = await response.text()
            return BeautifulSoup(src, 'lxml').findAll('a', class_= 'alllink')

async  def format_data(soup):
    castles = []
    lst = []
    for i in soup:
        lst.append(i.text)

    data = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}

    if GUILDNAME not in data.values():
        return 'Вы сегодня без замков'
    for k, v in data.items():
        if v == GUILDNAME:
            castles.append(k)

    return castles



async def main():
    await format_data(parse_castles())

"""
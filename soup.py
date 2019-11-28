#! /usr/bin/python3
#! coding: utf-8
#! Date: 2019-11-28
#! Author: Rea$on


import requests
from bs4 import BeautifulSoup


url = "https://pan.baidu.com/s/1Vi2g_l0A4UJFnuAaeZh7fg"
r = requests.get(url)
r.encoding = 'utf-8'

with open("ret.txt", 'w') as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title)
for link in soup.find_all('span'):
    print(link.get('class'))
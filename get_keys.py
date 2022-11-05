# pip install rich pyfiglet
import pyfiglet
import requests
from bs4 import BeautifulSoup

print(pyfiglet.figlet_format('CHelper', justify='center'))

keys = []

print('Входная информация типа (bitcoin/ethereum/BNB/tether)')
print('             Обязательно маленькими буквами          ')
token = input('>>>')

keys.append(token)
token1 = token
arr = []
for i in token1:
    arr.append(i)

arr[0] = arr[0].upper()

token1=''
for i in arr:
    token1+=i


keys.append(token1)

print(keys)






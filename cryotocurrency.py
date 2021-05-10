import requests
from bs4 import BeautifulSoup as bs

url='https://www.coindesk.com/price/bitcoin'
r=requests.get(url)

soup=bs(r.content,'html.parser')
price=soup.find('div',{'class':'price-large'})
print("bitcoin:",price.text)
percent=soup.find('span',{'class':'percent-value-text'})
percentage=float(percent.text)
if percentage>0:
    print('bitcoin increased today')
else:
    print('bitcoin decreased today')
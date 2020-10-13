import requests 
import bs4 
res=requests.get('https://www.stocktrak.com/trading/equities?ClientName=Wharton')
soup=bs4.BeautifulSoup(res.text,'lxml')
site=soup.select('.item up>span')
for i in site: 
    print(i.getText())

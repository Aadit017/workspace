import requests
import bs4
res=requests.get("https://www.stocktrak.com/dashboard?ClientName=Wharton")
soup=bs4.BeautifulSoup(res.text,'lxml')
site=soup.select('.count currency')
for item in site: 
    print(item.text)
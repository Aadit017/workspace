import requests 
import bs4 
res=requests.get('https://www.stocktrak.com/account/openpositions?ClientName=Wharton')
soup=bs4.BeautifulSoup(res.text,'lxml')
site=soup.select('profit-loss plus text-right')
print(site[0].getText())
import requests
import bs4 
res=requests.get('https://en.wikipedia.org/wiki/Elon_Musk')
soup=bs4.BeautifulSoup(res.text,'lxml')
first_item=soup.select('.toctext')[0]
f=open('webscrap.txt','w')
for counter,item in enumerate(soup.select('.toctext'),1): 
    print(item.getText())
    f.write(str(counter))
    f.write(item.getText())
    f.write('\n')
f.close()
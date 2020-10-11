import requests
import bs4
result=requests.get("http://www.example.com/")
print(result.text)
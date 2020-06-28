from bs4 import BeautifulSoup
import requests

url= "https://www.theguardian.com/environment/2020/jun/26/leading-scientist-criticises-uk-over-its-climate-record"
data= requests.get(url).text
data_storage= BeautifulSoup(data, features="html.parser").text

print(data_storage)


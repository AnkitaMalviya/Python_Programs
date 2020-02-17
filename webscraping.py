# import requests 
# from bs4 import BeautifulSoup 
  
# URL = "https://www.w3schools.com/tags/"
# r = requests.get(URL) 
# data=r.text         
# # print(data)
# soup = BeautifulSoup(data,"html5lib" )
# print(soup.prettify()) 




from bs4 import BeautifulSoup

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
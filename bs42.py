from bs4 import BeautifulSoup
import urllib2
import re


url = "https://github.com/search?q=suraj&type=Users"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "lxml")

#print soup.prettify()

#print (soup.find_all('li').get_text())
#for tag in soup.find_all(re.compile(r"([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}")):
#    print(tag)
#mydivs = soup.findAll("div", {"class": "stylelistrow"})


# user-list-info ml-2 min-width-0
# lis = soup.find_all('ul li', {"class": "mt-1 mt-md-0 mr-md-3"},text=True)
# lis = soup.findAll('a', {"class": "muted-link"})
# print lis
lis = soup.find_all('a', {"class": "menu-item"}, text=False)


##Getting Names
for list in lis:
    print(list.get_text())

##Getting All Links
#for link in soup.find_all('a', href=True):
#    print(link['href'])
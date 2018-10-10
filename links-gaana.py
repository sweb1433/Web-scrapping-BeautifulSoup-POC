####FOR GETTING ALL LINKS
from bs4 import BeautifulSoup
import urllib


array_Links =[]

#resp = urllib.urlopen("https://github.com/wialon/python-wialon/issues/8")

resp = urllib.urlopen("https://gaana.com/playlist/gaana-dj-sing-with-ed-sheeran-1")
soup = BeautifulSoup(resp,"lxml", from_encoding=resp.info().get('charset'))

for link in soup.find_all('a', href=True):
    array_Links.append(link['href'])
    for i in array_Links:
        if i == "javascript:void(0)":
            array_Links.remove(i)
    print(array_Links)



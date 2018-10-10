# from bs4 import BeautifulSoup
import urllib2
import re
 
html_page = urllib2.urlopen("https://facebook.com")
html = html_page.read()
# links = re.findall('"^http://"', html)

# print links
#url='<a href="http://www.ptop.se" target="_blank">http://www.ptop.se</a>'
r = re.compile('(?<=href=").*?(?=")')
print(r.findall(html))
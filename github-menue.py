import bs4 , requests

res = requests.get("https://github.com/search?q=suraj&type=Users")
soup = bs4.BeautifulSoup(res.text, 'lxml')
for link in soup.select('a[class="menu-item"]'):
    print link.get('href')
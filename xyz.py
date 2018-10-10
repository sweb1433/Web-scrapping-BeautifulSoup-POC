import csv
import requests
from bs4 import BeautifulSoup

base_url = "http://www.privredni-imenik.com/pretraga?abcd=&keyword=&cities_id=0&category_id=0&sub_category_id=0&page=1"
current_page = 1


with open('scrape_results.csv', 'w') as scrape_results:
    csvwriter = csv.writer(scrape_results)
    # csvwriter.writerows(['current_page', 'title1', 'adresa', 'kontakt'])

    while current_page < 200:
        url = base_url + str(current_page)
        r = requests.get(url)
        zute_soup = BeautifulSoup(r.text, 'html.parser')
        firme = zute_soup.findAll('div', {'class': 'jobs-item'})
        
        for title in firme:
            title1 = title.findAll('h6')[0].text
            adresa = title.findAll('div', {'class': 'description'})[0].text
            kontakt = title.findAll('div', {'class': 'description'})[1].text
            csvwriter.writerows([current_page, title1, adresa, kontakt])

        current_page += 1
import requests
from bs4 import BeautifulSoup
import csv

sitemap_url = 'https://www.investopedia.com/sitemap_1.xml'

response = requests.get(sitemap_url)

soup = BeautifulSoup(response.content, 'lxml')

locs = soup.select('url > loc')

with open('urls.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL']) 
    for loc in locs:
        url = loc.text
        writer.writerow([url])
        print(f'URL added: {url}')
print('URLs have been written to urls.csv.')
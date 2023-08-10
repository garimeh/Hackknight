import requests
from bs4 import BeautifulSoup
import csv

# URL of the sitemap
sitemap_url = 'https://www.investopedia.com/sitemap_1.xml'

# Send a GET request to the sitemap
response = requests.get(sitemap_url)

# Parse the XML content
soup = BeautifulSoup(response.content, 'lxml')

# Find all 'loc' tags within 'url' tags using CSS selectors
locs = soup.select('url > loc')

# Extract and print the URLs

with open('urls.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL']) 
    for loc in locs:
        url = loc.text
        writer.writerow([url])
        print(f'URL added: {url}')
print('URLs have been written to urls.csv.')
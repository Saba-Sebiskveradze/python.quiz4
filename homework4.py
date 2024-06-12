import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

with open('quotes.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])
    base_url = 'http://quotes.toscrape.com/page/{}'
    for page in range(1, 6):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='quote')

        for item in items:
            quote_text = item.find('span', class_='text').text.strip()
            author = item.find('small', class_='author').text.strip()

            writer.writerow([quote_text, author])
            print(f"Scraped: {quote_text}, {author}")

        sleep_time = randint(15, 20)
        time.sleep(sleep_time)


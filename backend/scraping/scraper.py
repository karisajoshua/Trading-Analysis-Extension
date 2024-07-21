import requests
from bs4 import BeautifulSoup

def scrape_news():
    # Example function to scrape news
    url = "https://example.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    for item in soup.find_all('div', class_='news-item'):
        title = item.find('h2').text
        summary = item.find('p').text
        news_items.append({'title': title, 'summary': summary})

    return news_items

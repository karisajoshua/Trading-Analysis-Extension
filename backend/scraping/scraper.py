import requests
from bs4 import BeautifulSoup

def scrape_news(url="https://example.com/news"):
    """
    Scrapes news articles from the specified URL.
    
    Args:
        url (str): The URL of the news page to scrape. Defaults to "https://example.com/news".
    
    Returns:
        list: A list of dictionaries, each containing the title and summary of a news item.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error parsing the HTML: {e}")
        return []

    news_items = []
    for item in soup.find_all('div', class_='news-item'):
        title_tag = item.find('h2')
        summary_tag = item.find('p')
        
        if title_tag and summary_tag:
            title = title_tag.text.strip()
            summary = summary_tag.text.strip()
            news_items.append({'title': title, 'summary': summary})

    return news_items

# Example usage:
# news = scrape_news()
# for item in news:
#     print(f"Title: {item['title']}\nSummary: {item['summary']}\n")



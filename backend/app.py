from flask import Flask, jsonify
from scraping.scraper import scrape_news

app = Flask(__name__)

@app.route('/api/scrape', methods=['GET'])
def scrape():
    data = scrape_news()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

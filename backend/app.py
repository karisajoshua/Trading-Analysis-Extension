import logging
from flask import Flask, jsonify, request, abort
from scraping.scraper import scrape_news

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/api/scrape', methods=['GET'])
def scrape():
    try:
        url = request.args.get('url', default="https://example.com/news", type=str)
        logger.info(f"Scraping news from URL: {url}")
        data = scrape_news(url)
        if not data:
            logger.warning(f"No data found for URL: {url}")
            abort(404, description="No news items found")
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error occurred while scraping: {e}")
        abort(500, description="Internal Server Error")

@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Not found', 'message': str(error.description)})
    response.status_code = 404
    return response

@app.errorhandler(500)
def internal_error(error):
    response = jsonify({'error': 'Internal Server Error', 'message': str(error.description)})
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run(debug=True)

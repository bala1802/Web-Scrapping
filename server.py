from flask import Flask, request, jsonify
from flask_cors import CORS
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400

        url = data.get('url')
        api_key = data.get('api_key')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        if not api_key:
            return jsonify({'error': 'API key is required'}), 400
        
        os.environ['FIRECRAWL_API_KEY'] = api_key
        crawler = FirecrawlApp()
        scrape_result = crawler.scrape_url(url)
        
        if not scrape_result or 'markdown' not in scrape_result:
            return jsonify({'error': 'Failed to scrape content'}), 500
            
        return jsonify({'content': scrape_result["markdown"]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Server starting on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000) 
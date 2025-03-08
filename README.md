# Web Page Scraper Chrome Extension

A Chrome extension that scrapes web pages using the FireCrawl API and saves the content as a text file. The extension works in conjunction with a local Flask server to process the scraping requests.

## Features

- Scrape any web page with one click
- Secure API key storage in Chrome
- Automatic file download of scraped content
- Clean and user-friendly interface
- Error handling and status feedback

## Prerequisites

- Python 3.x
- Google Chrome browser
- FireCrawl API key ([Get one here](https://firecrawl.co/))
- pip (Python package manager)

## Installation

### 1. Backend Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/bala1802/Web-Scrapping.git
   cd Web-Scrapping
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Chrome Extension Setup

1. Open Google Chrome
2. Navigate to `chrome://extensions/`
3. Enable "Developer mode" in the top right corner
4. Click "Load unpacked"
5. Select the directory containing the extension files (manifest.json, popup.html, etc.)

## Usage

1. Start the backend server:
   ```bash
   python server.py
   ```
   You should see: "Server starting on http://127.0.0.1:5000"

2. Using the extension:
   - Click the extension icon in Chrome
   - Enter your FireCrawl API key (it will be saved for future use)
   - Navigate to any webpage you want to scrape
   - Click "Scrape This Page"
   - The content will be automatically downloaded as `llm.txt`

## Project Structure

```
├── README.md
├── requirements.txt
├── server.py              # Flask backend server
├── manifest.json          # Chrome extension manifest
├── popup.html            # Extension popup interface
├── popup.js             # Extension frontend logic
└── background.js        # Extension background script
```

## Technical Details

- Backend: Flask (Python)
- Frontend: Chrome Extension (HTML, CSS, JavaScript)
- API: FireCrawl for web scraping
- Storage: Chrome Storage API for API key persistence
- Communication: HTTP/JSON between extension and backend

## Error Handling

The extension handles various error cases:
- Missing API key
- Server connection issues
- Scraping failures
- Invalid responses

## Security

- API keys are stored securely in Chrome's storage system
- All communication is local (127.0.0.1/localhost)
- No sensitive data is stored on disk except the API key in Chrome's secure storage

## Troubleshooting

1. **"Cannot connect to backend server" error**
   - Ensure the Flask server is running
   - Check if port 5000 is available
   - Verify no firewall is blocking the connection

2. **"API key is required" error**
   - Enter your FireCrawl API key in the extension popup
   - Make sure the key is valid

3. **Extension not working**
   - Reload the extension in chrome://extensions/
   - Restart the Flask server
   - Check Chrome's console for errors

## Contributing

Feel free to submit issues and enhancement requests!

# Mini Web Crawler 🕷️

This script is a lightweight recursive web crawler that explores URLs starting from a given root, up to a specified depth.

## 🧠 What It Does

- Starts from a root URL.
- Crawls all hyperlinks (`<a href="...">`) it finds.
- Recursively visits links (depth-limited).
- Tracks visited and not-visited URLs.
- Prints a basic crawl summary.

## ⚙️ How It Works

- Uses Python's `requests` and `BeautifulSoup` for HTTP requests and HTML parsing.
- Follows only links that start with `http`.
- Ignores duplicate URLs and skips previously visited ones.
- Gracefully handles timeouts and HTTP errors.

## 🔧 Usage

1. Install the requirements (if not already installed):

```bash
pip install requests beautifulsoup4
```

2.	Update the url variable in the script with your target:
```
url = 'http://example.com'
```

3.	Run the script
```
python sensycrawl.py
```

### Example output:
```
Crawling: http://example.com - Depth: 3
Crawling: http://example.com/about - Depth: 2
...
Not visited: http://example.com/broken-link
http://example.com Crawled successfully - Visited: 15, Not visited: 3
```


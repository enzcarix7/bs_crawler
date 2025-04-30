from bs4 import BeautifulSoup
from requests import Response, get

def crawl(url: str, depth: int, visited_urls: set = None, not_visited_urls: set = None):
    if visited_urls is None:
        visited_urls = set()
    if not_visited_urls is None:
        not_visited_urls = set()
    if url in visited_urls or depth < 0:
        return visited_urls
    print(f'Crawling: {url} - Depth: {depth}')
    visited_urls.add(url)
    try:
        response: Response = get(url, timeout=5)
        if response.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href: str = link['href']
                if href.startswith('http'):
                    crawl(href, depth - 1, visited_urls)
        else:
            not_visited_urls.add(url)
    except Exception as e:
        print(f'Error crawling {url}: {str(e)}')
        not_visited_urls.add(url)
    return visited_urls, not_visited_urls


url: str = 'x.x.x.x'
visited, not_visited_urls = crawl(url, 3)
print(f'{url} Crawled successfully - Visited: {len(visited)}, Not visited: {len(not_visited_urls)}')
for url in not_visited_urls:
    print(f'Not visited: {url}')

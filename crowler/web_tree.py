import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

logger = logging.getLogger(__name__)

class WebTree:
    def __init__(self, base_url, max_depth=3):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()  # Keeps track of visited URLs

    def fetch_page(self, url):
        """Fetches a page and parses its links."""
        try:
            logger.info(f"Fetching: {url}")
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def get_links(self, html, base_url):
        """Extracts and returns all unique internal links from the HTML."""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()

        for link in soup.find_all('a', href=True):
            href = link.get('href')
            # Resolve relative URLs to absolute ones
            absolute_url = urljoin(base_url, href)
            # Only add internal links (same domain)
            if urlparse(absolute_url).netloc == urlparse(base_url).netloc:
                links.add(absolute_url)
        
        return links

    def build_tree(self, url, depth=0):
        """Recursively builds the web tree starting from the given URL."""
        if depth > self.max_depth:
            return {}

        if url in self.visited:
            return {}

        self.visited.add(url)
        html = self.fetch_page(url)
        if html is None:
            return {}

        links = self.get_links(html, url)
        tree = {url: {}}

        for link in links:
            tree[url][link] = self.build_tree(link, depth + 1)

        return tree

    def get_web_tree(self):
        """Starts building the web tree from the base URL."""
        return self.build_tree(self.base_url)


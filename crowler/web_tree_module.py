import sys
import datetime
from web_tree import WebTree
from pprint import pprint
from scraper.exporter import DataExporter
import logging

logging.basicConfig(level=logging.INFO)

def crawl_website(base_url, max_depth=3):
    """
    Crawls the website starting from the base_url and prints the web tree.
    
    :param base_url: The base URL of the website to crawl
    :param max_depth: Maximum depth to crawl (default is 3)
    """
    # Create an instance of the WebTree class
    web_tree = WebTree(base_url, max_depth)
    
    # Get the web tree
    tree = web_tree.get_web_tree()
    
    # Print the web tree in a readable format
    pprint(tree, depth=2)

    return tree

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python web_tree_module.py <URL> [max_depth]")
        sys.exit(1)

    # Get the base URL and optional max depth from command line arguments
    base_url = sys.argv[1]
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    # Start crawling the website
    data = [crawl_website(base_url, max_depth)]
    x = datetime.datetime.now()
    DataExporter.to_json(data, f"{base_url}-{x.year}-{x.month}-{x.day}-{x.strftime("%X").replace(":","-")}.json")
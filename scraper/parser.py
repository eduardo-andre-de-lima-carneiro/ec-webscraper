from bs4 import BeautifulSoup
from .logger import get_logger

logger = get_logger(__name__)

class HTMLDataParser:
    @staticmethod
    def extract_text(soup, tag: str, attrs: dict = None):
        logger.info(f"Extracting <{tag}> elements with attributes: {attrs}")
        elements = soup.find_all(tag, attrs or {})
        results = [el.get_text(strip=True) for el in elements]
        logger.debug(f"Found {len(results)} <{tag}> element(s).")
        return results

    @staticmethod
    def extract_attribute(soup, tag: str, attribute: str, attrs: dict = None, base_url: str = ""):
        logger.info(f"Extracting attribute '{attribute}' from <{tag}> with attributes: {attrs}")
        elements = soup.find_all(tag, attrs or {})
        values = []

        for el in elements:
            val = el.get(attribute)
            if val:
                full_val = base_url + val if base_url and not val.startswith("http") else val
                values.append(full_val)

        logger.debug(f"Found {len(values)} attribute(s).")
        return values

    @staticmethod
    def extract_anchor_ids(links: list):
        anchors = [link.split("#")[-1] if "#" in link else None for link in links]
        logger.debug(f"Extracted {len(anchors)} anchor(s).")
        return anchors
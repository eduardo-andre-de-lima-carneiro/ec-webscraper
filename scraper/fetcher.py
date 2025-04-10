import requests
from .logger import get_logger

logger = get_logger(__name__)

class WebFetcher:
    @staticmethod
    def fetch(url: str) -> str:
        logger.info(f"Fetching URL: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

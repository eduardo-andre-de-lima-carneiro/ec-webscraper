from core.config import Config
from core.fetcher import HTMLFetcher, SeleniumFetcher
from core.parser import HTMLParser
from core.exporter import DataExporter

if __name__ == "__main__":
    if Config.HTML_SOURCE_TYPE == "file":
        html = HTMLFetcher.from_file(Config.HTML_SOURCE_PATH)
    elif Config.HTML_SOURCE_TYPE == "url":
        fetcher = SeleniumFetcher(
            url=Config.HTML_SOURCE_PATH,
            wait_for=Config.WAIT_FOR_SELECTOR,
            headless=Config.HEADLESS
        )
        html = fetcher.fetch()
    else:
        raise ValueError("Invalid HTML_SOURCE_TYPE. Use 'file' or 'url'.")

    parser = HTMLParser(html)
    vehicles = parser.parse_vehicles()
    DataExporter.to_json(vehicles, Config.EXPORT_PATH)

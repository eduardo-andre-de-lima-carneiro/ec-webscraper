from core.fetcher import HTMLFetcher, SeleniumFetcher
from core.parser import HTMLParser
from core.exporter import DataExporter
from core.config import get_config

def main():
    config = get_config()
    if config["HTML_SOURCE_TYPE"] == "file":
        html = HTMLFetcher.from_file(config["HTML_SOURCE_PATH"])
    elif config["HTML_SOURCE_TYPE"] == "url":
        fetcher = SeleniumFetcher(
            url=config["HTML_SOURCE_PATH"],
            wait_for=config["WAIT_FOR_SELECTOR"],
            headless=config["HEADLESS"]
        )
        html = fetcher.fetch()
    else:
        raise ValueError("Invalid HTML_SOURCE_TYPE. Use 'file' or 'url'.")

    parser = HTMLParser(html)
    vehicles = parser.parse_vehicles()
    DataExporter.to_json(vehicles, config["EXPORT_PATH"])

if __name__ == "__main__":
    main()
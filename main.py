import logging
import os
from dotenv import load_dotenv
from pathlib import Path
from scraper.fetcher import WebFetcher
from scraper.parser import HTMLDataParser
from scraper.exporter import DataExporter
from bs4 import BeautifulSoup

def main():
    load_dotenv()
    url = os.getenv("URL")
    html = WebFetcher.fetch(url)

    if html:
        data = extract_data(html)

        DataExporter.to_csv(data, "output.csv")
        DataExporter.to_json(data, "output.json")
        print("✅ Export done.")
    else:
        print("❌ Failed to retrieve HTML.")

def extract_data(html):
        load_dotenv()
        block_class = os.getenv("BLOCK_CLASS")
        name_class = os.getenv("NAME_CLASS")
        info_class = os.getenv("INFO_CLASS")
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        soup = BeautifulSoup(html, "html.parser")
        data = []
        data_blocks = soup.find_all("div", class_=block_class)

        print(data_blocks)

        for block in data_blocks:
            try:
                #Name
                name = block.find("a", class_=name_class).get_text(strip=True).replace("®", "")
                info_container = block.find_next("div", class_=info_class)

                # Price
                # price_span = info_container.select_one("span[data-pricing-template]")
                # price = price_span.get("data-pricing-template", "").replace("{price}", "").strip()

                # Badge
                badge_label = info_container.find("span", class_="badges-label")
                badge_text = badge_label.get_text(strip=True) if badge_label else "N/A"

                data.append({
                    "name": name,
                    "badge": badge_text
                })
            except Exception as e:
                logger.warning(f"Could not parse a data block: {e}")
                continue

        return data

if __name__ == "__main__":
    main()
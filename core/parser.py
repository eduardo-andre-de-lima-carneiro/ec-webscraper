from bs4 import BeautifulSoup
from .models import Vehicle
from .utils import get_logger

logger = get_logger("parser")

class HTMLParser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    def parse_vehicles(self):
        vehicles = []
        tiles = self.soup.select(".vehicle-box")

        for tile in tiles:
            try:
                # Get name
                name_tag = tile.select_one(".np-desc") #(".nameplate-name a")
                name = name_tag.get_text(strip=True).replace("®", "")

                # Get year from data attribute
                # year = tile.get("data-link-context", "")
                # year = year.split('"year":"')[1].split('"')[0] if "year" in year else "N/A"
                year_tag = tile.select_one(".np-year")
                year = year_tag.get_text(strip=True) or "N/A" #(".nameplate-name a")

                # Get price (if exists)
                price = "N/A"
                price_tag = tile.select_one(".price-box")
                if price_tag:
                    price = price_tag.get_text(strip=True).replace("À partir de","").replace("$1","") or "N/A"

                vehicles.append(Vehicle(name=name, year=year, price=price))
            except Exception as e:
                logger.warning(f"⚠️ Failed to parse vehicle: {e}")
        return vehicles

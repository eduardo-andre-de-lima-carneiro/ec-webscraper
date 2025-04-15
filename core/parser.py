import re
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
                name_tag = tile.select_one(".np-desc")
                name = name_tag.get_text(strip=True).replace("®", "") if name_tag else "N/A"

                year_tag = tile.select_one(".np-year")
                year = year_tag.get_text(strip=True) if year_tag else "N/A"

                price_tag = tile.select_one(".price-box")
                price = (
                    re.sub(r"[^0-9\.,]", "", price_tag.get_text(strip=True)) or "N/A"
                )
                vehicle = Vehicle(name=name, year=year, price=price)
                if vehicle.is_valid():
                    vehicles.append(vehicle)
            except Exception as e:
                logger.warning(f"⚠️ Failed to parse vehicle: {e}")
        return vehicles

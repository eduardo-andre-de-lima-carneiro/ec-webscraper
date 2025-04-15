from dataclasses import dataclass
import logging

logger = logging.getLogger("models")

@dataclass
class Vehicle:
    name: str
    year: str
    price: str = "N/A"

    def is_valid(self):
        if self.name == "N/A" or self.year == "N/A":
            logger.warning(f"⚠️ Invalid Vehicle Data: {self}")
            return False
        return True

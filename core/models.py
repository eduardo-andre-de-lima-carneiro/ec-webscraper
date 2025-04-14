from dataclasses import dataclass

@dataclass
class Vehicle:
    name: str
    year: str
    price: str = "N/A"
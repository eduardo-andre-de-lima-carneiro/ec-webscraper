import pytest
from core.parser import HTMLParser
from core.models import Vehicle

def test_vehicle_parsing():
    html = open("tests/sample.html", encoding="utf-8").read()
    parser = HTMLParser(html)
    vehicles = parser.parse_vehicles()

    assert isinstance(vehicles, list)
    assert all(isinstance(v, Vehicle) for v in vehicles)
    assert any("Mustang" in v.name for v in vehicles)

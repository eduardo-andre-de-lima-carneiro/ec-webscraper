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

def test_parser_extracts_vehicles():
    html = """
    <div class="vehicle-tile-inner" data-link-context='{"year":"2025"}'>
        <div class="nameplate-name"><a>Bronco Sport<sup>®</sup></a></div>
        <span data-pricing-template="{price}">À partir de 39 999$</span>
    </div>
    """
    parser = HTMLParser(html)
    vehicles = parser.parse_vehicles()
    assert len(vehicles) == 1
    assert "Bronco" in vehicles[0].name

def test_parser_with_empty_html():
    parser = HTMLParser("")
    vehicles = parser.parse_vehicles()
    assert vehicles == []
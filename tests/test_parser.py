from core.parser import HTMLParser
from core.models import Vehicle

def test_parser_new_structure():
    html = """
    <div class="vehicle-box">
        <div class="np-year">2025</div>
        <div class="np-desc">Explorer</div>
        <div class="price-box">À partir de 45 000$</div>
    </div>
    <div class="vehicle-box">
        <div class="np-year">2024</div>
        <div class="np-desc">Edge</div>
        <div class="price-box">À partir de 39 999$</div>
    </div>
    """
    parser = HTMLParser(html)
    vehicles = parser.parse_vehicles()

    assert len(vehicles) == 2
    assert vehicles[0].name == "Explorer"
    assert vehicles[0].year == "2025"
    assert vehicles[0].price == "45000"
    assert vehicles[1].name == "Edge"
    assert vehicles[1].year == "2024"
    assert vehicles[1].price == "39999"

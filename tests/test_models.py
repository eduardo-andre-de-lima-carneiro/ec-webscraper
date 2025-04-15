from core.models import Vehicle

def test_vehicle_model():
    v = Vehicle(name="Bronco", year="2025", price="39999")
    assert v.name == "Bronco"
    assert v.year == "2025"
    assert v.price == "39999"

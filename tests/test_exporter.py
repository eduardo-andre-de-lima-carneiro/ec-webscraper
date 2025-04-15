import os
import json
from core.exporter import DataExporter
from core.models import Vehicle

def test_export_to_json(tmp_path):
    vehicles = [Vehicle("Test", "2024", "29999")]
    export_file = tmp_path / "test.json"
    DataExporter.to_json(vehicles, str(export_file))
    
    assert export_file.exists()
    
    with open(export_file, encoding="utf-8") as f:
        data = json.load(f)
        assert data[0]["name"] == "Test"

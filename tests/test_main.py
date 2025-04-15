import os
from unittest.mock import patch, MagicMock
import main as main_module  # This works with PYTHONPATH=.

@patch("core.fetcher.HTMLFetcher.from_file")
@patch("core.parser.HTMLParser.parse_vehicles")
@patch("core.exporter.DataExporter.to_json")
def test_main_file_mode(mock_export_json, mock_parse, mock_fetch):
    os.environ["HTML_SOURCE_TYPE"] = "file"
    os.environ["HTML_SOURCE_PATH"] = "sample.html"
    os.environ["EXPORT_PATH"] = "vehicles.json"

    import importlib
    import core.config
    importlib.reload(core.config)

    mock_fetch.return_value = "<html><div class='vehicle-box'></div></html>"
    mock_parse.return_value = [
        {"name": "Escape", "year": "2025", "price": "45 000$"}
    ]

    main_module.main()

    mock_fetch.assert_called_once()
    mock_parse.assert_called_once()
    mock_export_json.assert_called_once()

@patch("core.fetcher.SeleniumFetcher.fetch")
@patch("core.parser.HTMLParser.parse_vehicles")
@patch("core.exporter.DataExporter.to_json")
def test_main_url_mode(mock_export_json, mock_parse, mock_fetch):
    os.environ["HTML_SOURCE_TYPE"] = "url"
    os.environ["HTML_SOURCE_PATH"] = "https://fr.ford.ca/suvs-crossovers/"
    os.environ["WAIT_FOR_SELECTOR"] = ".vehicle-box"
    os.environ["HEADLESS"] = "true"
    os.environ["EXPORT_PATH"] = "vehicles.json"

    mock_fetch.return_value = "<html><div class='vehicle-box'></div></html>"
    mock_parse.return_value = [
        {"name": "Bronco", "year": "2024", "price": "38 999$"}
    ]

    main_module.main()

    mock_fetch.assert_called_once()
    mock_parse.assert_called_once()
    mock_export_json.assert_called_once()

def test_main_invalid_source_type(monkeypatch):
    monkeypatch.setenv("HTML_SOURCE_TYPE", "invalid")
    try:
        main_module.main()
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "Invalid HTML_SOURCE_TYPE" in str(e)

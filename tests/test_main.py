import os
from unittest.mock import patch, MagicMock
import main as main_module

@patch("ec-webscraper.main.HTMLFetcher.from_file")
@patch("ec-webscraper.main.HTMLParser.parse_vehicles")
@patch("ec-webscraper.main.DataExporter.to_json")
def test_main_file_pipeline(mock_export, mock_parse, mock_fetch):
    os.environ["HTML_SOURCE_TYPE"] = "file"
    os.environ["HTML_SOURCE_PATH"] = "dummy.html"
    os.environ["EXPORT_PATH"] = "out.json"

    mock_fetch.return_value = "<html>valid html</html>"
    mock_parse.return_value = [{"name": "Test", "year": "2024", "price": "10000"}]

    main_module.main()

    mock_fetch.assert_called_once()
    mock_parse.assert_called_once()
    mock_export.assert_called_once()

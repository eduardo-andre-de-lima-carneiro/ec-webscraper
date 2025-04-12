import unittest
from unittest.mock import patch, MagicMock
from main import main, extract_data

class TestMainScript(unittest.TestCase):

    @patch("main.os.getenv")
    @patch("main.WebFetcher.fetch")
    @patch("main.DataExporter.to_csv")
    @patch("main.DataExporter.to_json")
    def test_main_successful_flow(self, mock_json, mock_csv, mock_fetch, mock_getenv):
        # Setup mocks
        mock_getenv.side_effect = lambda key: {
            "URL": "http://fake-url.com",
            "BLOCK_CLASS": "vehicle-name-container",
            "NAME_CLASS": "nameplate-name",
            "INFO_CLASS": "vehicle-info"
        }.get(key)

        # Fake HTML snippet
        mock_html = '''
        <div class="vehicle-name-container">
            <div class="nameplate-name">
                Maverick<sup>®</sup>
            </div>
            <div class="vehicle-info">
                <span data-pricing-template="{price}">30,000$</span>
                <span class="badges-label">Hybride disponible</span>
            </div>
        </div>
        '''
        mock_fetch.return_value = mock_html

        main()

        mock_fetch.assert_called_once()
        mock_csv.assert_called_once()
        mock_json.assert_called_once()

    def test_extract_data_from_html(self):
        sample_html = '''
        <div class="vehicle-name-container">
            <div class="nameplate-name">Maverick<sup>®</sup></div>
            <div class="vehicle-info">
                <span data-pricing-template="{price}">30,000$</span>
                <span class="badges-label">Hybride disponible</span>
            </div>
        </div>
        '''

        with patch("main.os.getenv") as mock_getenv:
            mock_getenv.side_effect = lambda key: {
                "BLOCK_CLASS": "vehicle-name-container",
                "NAME_CLASS": "nameplate-name",
                "INFO_CLASS": "vehicle-info"
            }.get(key)

            result = extract_data(sample_html)

            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["name"], "Maverick")
            self.assertEqual(result[0]["badge"], "Hybride disponible")

if __name__ == "__main__":
    unittest.main()
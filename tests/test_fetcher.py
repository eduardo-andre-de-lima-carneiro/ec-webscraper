import unittest
from unittest.mock import patch, MagicMock
from scraper.fetcher import WebFetcher

class TestWebFetcher(unittest.TestCase):
    @patch("scraper.fetcher.requests.get")
    def test_fetch_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Hello</body></html>"
        mock_get.return_value = mock_response

        result = WebFetcher.fetch("http://example.com")
        self.assertIn("Hello", result)

    @patch('scraper.fetcher.requests.get')
    def test_fetch_failure(self, mock_get):
        mock_get.side_effect = Exception("Request failed")
        with self.assertRaises(Exception) as context:
            WebFetcher.fetch("http://example.com")
        
        self.assertEqual(str(context.exception), "Request failed")

if __name__ == "__main__":
    unittest.main()
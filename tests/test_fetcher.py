import pytest
from unittest.mock import patch, MagicMock
from core.fetcher import HTMLFetcher, SeleniumFetcher

def test_fetch_from_file(tmp_path):
    file = tmp_path / "sample.html"
    file.write_text("<html><body>test</body></html>", encoding="utf-8")
    content = HTMLFetcher.from_file(str(file))
    assert "test" in content

@patch("core.fetcher.webdriver.Chrome")
@patch("core.fetcher.ChromeDriverManager")
def test_selenium_fetcher_mocked(mock_driver_manager, mock_chrome):
    fake_driver = MagicMock()
    fake_driver.page_source = "<html><body><div class='vehicle-tile-inner'></div></body></html>"
    mock_chrome.return_value = fake_driver

    fetcher = SeleniumFetcher("https://example.com", wait_for=".vehicle-tile-inner", headless=True)
    html = fetcher.fetch()

    assert "<div class='vehicle-tile-inner'>" in html
    fake_driver.get.assert_called_once()
    fake_driver.quit.assert_called_once()
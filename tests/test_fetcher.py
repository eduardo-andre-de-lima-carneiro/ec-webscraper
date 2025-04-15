import pytest
from unittest.mock import patch, MagicMock
from core.fetcher import SeleniumFetcher

@patch("selenium.webdriver.Chrome")
@patch("webdriver_manager.chrome.ChromeDriverManager")
def test_selenium_fetcher_mocked(mock_driver_manager, mock_chrome):
    fake_driver = MagicMock()
    fake_driver.page_source = "<html><body><div class='vehicle-tile-inner'></div></body></html>"
    mock_chrome.return_value = fake_driver

    fetcher = SeleniumFetcher("https://example.com", wait_for=".vehicle-tile-inner", headless=True)
    html = fetcher.fetch()

    assert "<div class='vehicle-tile-inner'>" in html
    fake_driver.get.assert_called_once()
    fake_driver.quit.assert_called_once()

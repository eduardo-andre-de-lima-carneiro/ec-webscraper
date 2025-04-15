from unittest.mock import patch, MagicMock
from core.fetcher import HTMLFetcher

def test_fetch_from_file(tmp_path):
    file = tmp_path / "sample.html"
    file.write_text("<html><body>test</body></html>", encoding="utf-8")
    content = HTMLFetcher.from_file(str(file))
    assert "test" in content

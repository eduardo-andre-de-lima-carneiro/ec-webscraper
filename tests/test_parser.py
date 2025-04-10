import unittest
from bs4 import BeautifulSoup
from scraper.parser import HTMLDataParser

class TestHTMLDataParser(unittest.TestCase):
    def setUp(self):
        self.html = '''
        <html>
            <body>
                <h2 class="headline bri-txt ff-b title-three">Bronco Sport</h2>
                <h2 class="headline bri-txt ff-b title-three">Escape</h2>
                <a class="cta one btn-icon" href="/new-suvs-crossovers/#bronco">En savoir plus</a>
                <a class="cta one btn-icon" href="/new-suvs-crossovers/#escape">En savoir plus</a>
            </body>
        </html>
        '''
        self.soup = BeautifulSoup(self.html, "html.parser")

    def test_extract_text(self):
        results = HTMLDataParser.extract_text(self.soup, "h2", {"class": "headline bri-txt ff-b title-three"})
        self.assertEqual(results, ["Bronco Sport", "Escape"])

    def test_extract_attribute(self):
        links = HTMLDataParser.extract_attribute(self.soup, "a", "href", {"class": "cta one btn-icon"}, "https://example.com")
        self.assertEqual(links, [
            "https://example.com/new-suvs-crossovers/#bronco",
            "https://example.com/new-suvs-crossovers/#escape"
        ])

    def test_extract_anchor_ids(self):
        links = [
            "https://example.com/new-suvs-crossovers/#bronco",
            "https://example.com/new-suvs-crossovers/#escape"
        ]
        anchors = HTMLDataParser.extract_anchor_ids(links)
        self.assertEqual(anchors, ["bronco", "escape"])

if __name__ == "__main__":
    unittest.main()
from scraper.fetcher import WebFetcher
from scraper.parser import HTMLDataParser
from scraper.exporter import DataExporter
from bs4 import BeautifulSoup

def main():
    url = "https://example.com"
    base_url = "https://example.com"
    html = WebFetcher.fetch(url)

    if html:
        soup = BeautifulSoup(html, "html.parser")

        models = HTMLDataParser.extract_text(soup, "h2", {"class": "headline bri-txt ff-b title-three"})
        links = HTMLDataParser.extract_attribute(soup, "a", "href", {"class": "cta one btn-icon"}, base_url)
        anchors = HTMLDataParser.extract_anchor_ids(links)

        data = [{"Model": m, "Link": l, "Anchor": a} for m, l, a in zip(models, links, anchors)]

        DataExporter.to_csv(data, "output.csv")
        DataExporter.to_json(data, "output.json")
        print("✅ Export done.")
    else:
        print("❌ Failed to retrieve HTML.")

if __name__ == "__main__":
    main()
import unittest
import os
import json
import pandas as pd
from scraper.exporter import DataExporter

class TestExporter(unittest.TestCase):
    def setUp(self):
        self.test_data_dicts = [
            {"Model": "Bronco Sport", "Link": "https://example.com#bronco", "Anchor": "bronco"},
            {"Model": "Escape", "Link": "https://example.com#escape", "Anchor": "escape"}
        ]

        self.test_data_tuples = [
            ("Bronco Sport", "https://example.com#bronco", "bronco"),
            ("Escape", "https://example.com#escape", "escape")
        ]

        self.columns = ["Model", "Link", "Anchor"]

    def test_export_csv_from_dicts(self):
        DataExporter.to_csv(self.test_data_dicts, "test_dicts.csv")
        self.assertTrue(os.path.exists("test_dicts.csv"))
        df = pd.read_csv("test_dicts.csv")
        self.assertEqual(df.iloc[0]["Model"], "Bronco Sport")
        os.remove("test_dicts.csv")

    def test_export_csv_from_tuples(self):
        DataExporter.to_csv(self.test_data_tuples, "test_tuples.csv", columns=self.columns)
        self.assertTrue(os.path.exists("test_tuples.csv"))
        df = pd.read_csv("test_tuples.csv")
        self.assertEqual(df.iloc[1]["Anchor"], "escape")
        os.remove("test_tuples.csv")

    def test_export_json(self):
        DataExporter.to_json(self.test_data_dicts, "test.json")
        self.assertTrue(os.path.exists("test.json"))
        with open("test.json", "r", encoding="utf-8") as f:
            content = json.load(f)
            self.assertEqual(content[0]["Anchor"], "bronco")
        os.remove("test.json")

    def test_json_export_raises_type_error(self):
        with self.assertRaises(TypeError):
            DataExporter.to_json(self.test_data_tuples, "invalid.json")

    def test_csv_export_raises_type_error(self):
        with self.assertRaises(TypeError):
            DataExporter.to_csv("not_a_list", "invalid.csv")

if __name__ == "__main__":
    unittest.main()

import pandas as pd
import json
from .logger import get_logger

logger = get_logger(__name__)

class DataExporter:
    @staticmethod
    def to_csv(data, filename: str, columns=None):
        logger.info(f"Exporting data to CSV: {filename}")
        if isinstance(data, list) and data:
            if isinstance(data[0], dict):
                df = pd.DataFrame(data)
            elif isinstance(data[0], tuple):
                if columns is None:
                    raise ValueError("Column names must be provided when exporting tuple data.")
                df = pd.DataFrame(data, columns=columns)
            else:
                raise TypeError("Data must be a list of dicts or tuples.")

            df.to_csv(filename, index=False, encoding='utf-8')
            logger.info("✅ CSV export completed.")
        else:
            logger.warning("⚠️ No data provided for CSV export.")
            raise TypeError("No data provided for CSV export.")

    @staticmethod
    def to_json(data, filename: str, indent: int = 2):
        logger.info(f"Exporting data to JSON: {filename}")
        if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            logger.error("❌ JSON export requires a list of dictionaries.")
            raise TypeError("Data must be a list of dictionaries.")

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
            logger.info("✅ JSON export completed.")
        except Exception as e:
            logger.error(f"Error writing JSON: {e}")
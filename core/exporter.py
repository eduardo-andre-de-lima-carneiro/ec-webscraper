import json
from pathlib import Path
from .models import Vehicle
from .utils import get_logger

logger = get_logger("exporter")

class DataExporter:
    @staticmethod
    def to_json(vehicles: list[Vehicle], output_path: str):
        data = [v.__dict__ for v in vehicles]
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"✅ Exported {len(vehicles)} vehicles to {output_path}")

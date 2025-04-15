import os
from core import config
from importlib import reload
import core.config as config_module

def test_env_loaded():
    assert config.Config.HTML_SOURCE_TYPE in ["file", "url"]
    assert isinstance(config.Config.EXPORT_PATH, str)

def test_config_defaults_on_missing_env(monkeypatch):
    monkeypatch.delenv("EXPORT_PATH", raising=False)
    reload(config_module)
    assert config_module.Config.EXPORT_PATH == "vehicles.json"

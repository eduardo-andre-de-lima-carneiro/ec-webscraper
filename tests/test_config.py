import os
from core import config as config_module
from importlib import reload

def test_env_loaded():
    config_data = config_module.get_config()  # Use the function-based config
    assert config_data["HTML_SOURCE_TYPE"] in ["file", "url"]
    assert isinstance(config_data["EXPORT_PATH"], str)

def test_config_defaults_on_missing_env(monkeypatch):
    # Remove the environment variable temporarily
    monkeypatch.delenv("EXPORT_PATH", raising=False)
    
    # Reload config to get updated environment variables
    config_data = config_module.get_config()
    
    assert config_data["EXPORT_PATH"] == "vehicles.json"
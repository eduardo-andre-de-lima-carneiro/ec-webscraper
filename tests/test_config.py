from core import config

def test_env_loaded():
    assert config.Config.HTML_SOURCE_TYPE in ["file", "url"]
    assert isinstance(config.Config.EXPORT_PATH, str)

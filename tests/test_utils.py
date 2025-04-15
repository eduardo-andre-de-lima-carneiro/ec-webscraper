from core.utils import get_logger

def test_logger_setup():
    logger = get_logger("test_logger")
    assert logger.name == "test_logger"
    logger.info("Logger works!")

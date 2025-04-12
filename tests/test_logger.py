import unittest
import logging
from io import StringIO
from contextlib import redirect_stderr
from scraper.logger import get_logger  # Replace with your actual module name

class TestLoggerUtility(unittest.TestCase):

    def test_logger_creation(self):
        logger_name = "testLogger"
        logger = get_logger(logger_name)

        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.name, logger_name)
        self.assertEqual(logger.level, logging.DEBUG)
        self.assertTrue(logger.hasHandlers())

    def test_logger_no_duplicate_handlers(self):
        logger_name = "duplicateTest"
        logger1 = get_logger(logger_name)
        handler_count_1 = len(logger1.handlers)

        logger2 = get_logger(logger_name)
        handler_count_2 = len(logger2.handlers)

        self.assertEqual(logger1, logger2)
        self.assertEqual(handler_count_1, handler_count_2)
        self.assertEqual(handler_count_1, 1)

    def test_logger_output_format(self):
        stream = StringIO()
        logger = get_logger("formatTest")

        # Remove default handlers to avoid duplication
        logger.handlers = []

        # Attach our test handler
        handler = logging.StreamHandler(stream)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logger.setLevel(logging.DEBUG)
        logger.info("This is a test message")

        output = stream.getvalue()
        self.assertIn("formatTest", output)
        self.assertIn("INFO", output)
        self.assertIn("This is a test message", output)

if __name__ == "__main__":
    unittest.main()
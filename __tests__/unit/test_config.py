# tests/unit/test_config.py
from config import config, DevelopmentConfig, ProductionConfig
import os

def test_config_debug_setting():
    # Check that the config is set based on the FLASK_ENV environment variable.
    os.environ["FLASK_ENV"] = "development"
    dev_config = DevelopmentConfig()
    assert dev_config.DEBUG is True

    os.environ["FLASK_ENV"] = "production"
    prod_config = ProductionConfig()
    # Production config doesn't override DEBUG so it should be False
    assert prod_config.DEBUG is False

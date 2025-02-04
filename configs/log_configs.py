import io
import json
import logging
import logging.config
import os
import sys


def load_logging_config(file_path) -> dict:
    """Loads the JSON config from the given file path"""
    with open(file_path, "r") as f:
        return json.load(f)


def load_log_dictConfig() -> None:
    """Loads and sets up logging config if not already configured"""
    # log_dir = os.path.join(os.path.dirname(__file__), "logs")
    log_dir = os.path.join("logs")
    # print(f"log_dir: {log_dir}")

    # ✅ Ensure the logs directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_configs = load_logging_config(os.path.join(os.path.dirname(__file__), "log_Configs.json"))

    logging.config.dictConfig(log_configs)


# Run setup when the module is imported
load_log_dictConfig()

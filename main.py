#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the main module of the application.
It serves as the entry point for execution.
It initializes the application and handles command-line arguments.
"""

# Standard Libraries
import argparse
import logging
import os
import sys

# My Modules
from preflight import check_environment

__author__ = "Your Name"
__email__ = "joshua.kiley.dev@gmail.com"
__version__ = "1.0.0"
__license__ = "MIT"

# CONSTANTS
APP_NAME = "messy-desk"
DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
DESKTOP_DIR = os.path.join(os.path.expanduser("~"), "Desktop")
DOCUMENTS_DIR = os.path.join(os.path.expanduser("~"), "Documents")
PICTURES_DIR = os.path.join(os.path.expanduser("~"), "Pictures")
VIDEOS_DIR = os.path.join(os.path.expanduser("~"), "Videos")
MUSIC_DIR = os.path.join(os.path.expanduser("~"), "Music")
ARCHIVES_DIR = os.path.join(os.path.expanduser("~"), "Archives")
EXECUTABLES_DIR = os.path.join(os.path.expanduser("~"), "Executables")

TARGET_EXPORT_FOLDERS = {"downloads": DOWNLOADS_DIR, "desktop": DESKTOP_DIR}
TARGET_IMPORT_FOLDERS = {
    "documents": DOCUMENTS_DIR,
    "pictures": PICTURES_DIR,
    "videos": VIDEOS_DIR,
    "music": MUSIC_DIR,
    "archives": ARCHIVES_DIR,
    "executables": EXECUTABLES_DIR,
}
TARGET_EXTENSIONS = {
    "documents": [".pdf", ".docx", ".txt", ".md"],
    "pictures": [".jpg", ".jpeg", ".png", ".gif"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "music": [".mp3", ".wav", ".flac"],
    "archives": [".zip", ".tar", ".gz", ".rar"],
    "executables": [".exe", ".sh", ".bat", ".app"],
}

DEFAULT_LOG_FILE = os.path.join(
    os.path.expanduser("~"), "logs", APP_NAME, f"{APP_NAME}.log"
)


def setup_logging(log_file_path: str) -> None:
    """Configures a named logger for the application.

    Creates the log directory if it does not exist and sets up a logger
    with both file and stream handlers.

    Args:
        log_file_path (str): The full path to the log file.
    """
    log_directory = os.path.dirname(log_file_path)
    os.makedirs(log_directory, exist_ok=True)

    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.DEBUG)

    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(log_formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.propagate = False


def main() -> int:
    """Parses arguments, sets up logging, and runs the main application logic.

    This function serves as the primary entry point. It handles command-line
    argument parsing for configuration, initializes the logging system, and
    executes the core preflight checks of the application.

    Returns:
        int: An exit code, 0 for success and 1 for failure.

    Raises:
        EnvironmentError: If a critical preflight check fails.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Messy Desk Application")
    parser.add_argument(
        "--log-file",
        default=DEFAULT_LOG_FILE,
        help=f"Path to the log file. Defaults to {DEFAULT_LOG_FILE}",
    )
    args = parser.parse_args()

    # Setup logging system
    setup_logging(args.log_file)

    try:
        logging.info(f"Starting {APP_NAME} version {__version__}")
        logging.info("Performing preflight environment checks...")
        check_environment()
        logging.info("✓ Environment checks passed successfully.")
    except EnvironmentError as e:
        logging.error(f"A critical environment check failed: {e}")
        logging.debug("Exiting with status code 1.")
        return 1

    logging.info("Application finished successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

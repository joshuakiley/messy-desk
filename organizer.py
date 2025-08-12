"""
This module contains the core file organization logic.
"""

import logging

import config

logger = logging.getLogger(config.APP_NAME)


def sort_folder(source_folder_path: str):
    """
    Sorts files in a given source folder into destination folders
    based on their extensions.

    Args:
        source_folder_path (str): The absolute path to the folder to sort.
    """
    logger.info(f"Scanning source folder: {source_folder_path}")

    # TODO 1: Loop through all items in the source_folder_path.
    # Use os.listdir().

    # TODO 2: For each item, create its full path and check if it's a file.
    # Use os.path.join() and os.path.isfile(). Ignore directories.

    # TODO 3: Get the file's extension.
    # Use os.path.splitext(). Remember it returns a tuple (name, ext).

    # TODO 4: Find which category the extension belongs to (e.g., "pictures").
    # Loop through the config.TARGET_EXTENSIONS dictionary.

    # TODO 5: If a category is found, determine the destination path.
    # Use the category to look up the path in config.DESTINATION_FOLDERS.

    # TODO 6: Move the file to its new home.
    # Use shutil.move(source_path, destination_path).
    # Be sure to log the action! logger.info(f"Moving {filename}...")

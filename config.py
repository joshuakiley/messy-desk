"""
This module contains the configuration constants for the Messy Desk application.
"""

import os

# --- APP METADATA ---
APP_NAME = "messy-desk"
DEFAULT_LOG_FILE = os.path.join(
    os.path.expanduser("~"), "logs", APP_NAME, f"{APP_NAME}.log"
)

# --- FOLDER PATHS ---
DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
DESKTOP_DIR = os.path.join(os.path.expanduser("~"), "Desktop")
DOCUMENTS_DIR = os.path.join(os.path.expanduser("~"), "Documents")
PICTURES_DIR = os.path.join(os.path.expanduser("~"), "Pictures")
VIDEOS_DIR = os.path.join(os.path.expanduser("~"), "Videos")
MUSIC_DIR = os.path.join(os.path.expanduser("~"), "Music")
ARCHIVES_DIR = os.path.join(os.path.expanduser("~"), "Archives")
EXECUTABLES_DIR = os.path.join(os.path.expanduser("~"), "Executables")

# --- FOLDER MAPPINGS ---
SOURCE_FOLDERS = {
    "downloads": DOWNLOADS_DIR,
    "desktop": DESKTOP_DIR,
}
DESTINATION_FOLDERS = {
    "documents": DOCUMENTS_DIR,
    "pictures": PICTURES_DIR,
    "videos": VIDEOS_DIR,
    "music": MUSIC_DIR,
    "archives": ARCHIVES_DIR,
    "executables": EXECUTABLES_DIR,
}

# --- FILE EXTENSION MAPPINGS ---
TARGET_EXTENSIONS = {
    "documents": [".pdf", ".docx", ".txt", ".md"],
    "pictures": [".jpg", ".jpeg", ".png", ".gif"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "music": [".mp3", ".wav", ".flac"],
    "archives": [".zip", ".tar", ".gz", ".rar"],
    "executables": [".exe", ".sh", ".bat", ".app"],
}

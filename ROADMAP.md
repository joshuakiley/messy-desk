# Messy Desk Project Roadmap

This document will capture all planning, ideas, and steps for improving and maintaining the Messy Desk project. Each section will be updated as we clarify requirements and make decisions.

## Step 0: Intake & Constraints

- **Python Version:** 3.9+ (tested on 3.9, 3.10, 3.11; recommended for best compatibility and modern features)
- **Available Libraries:** Standard library only, unless specified. (e.g., pathlib, argparse, logging)
- **Target Environment:** CLI utility for Linux, macOS, Windows; User Interface (GUI)
- **Known Limitations:** Some features may require additional permissions or may not work on older OS versions.
- **Sample Inputs/Outputs:**
  - Manual mode: User runs the app from the command line or UI to organize folders on demand.
    - Example input: User executes `python3 main.py --sort downloads` or clicks 'Sort Downloads' in the UI.
    - Example output: Files in Downloads are moved into categorized subfolders; log file is generated.
    - Before: Downloads folder contains `photo1.jpg`, `statement_March.pdf`, `bills_April.xlsx`, `notes.txt`
    - After: `photo1.jpg` → `/Photos`, `statement_March.pdf` → `/Documents/Statements`, `bills_April.xlsx` → `/Documents/Bills`, `notes.txt` remains in Downloads
    - UI mockup: [Sort Downloads] button, [View Log] button
  - Event-driven mode: App is configured to watch Downloads and Desktop folders, but only acts when notified by the system of new activity (not constant polling).
    - Example input: System event triggers app when a new file is added to Downloads (e.g., `vacation.png`)
    - Example output: `vacation.png` is moved to `/Photos`; user receives notification: "1 file sorted to Photos."
    - UI mockup: Notification banner: "Files sorted! View details in log."
- **Error Conditions:**
  - On error, stop all actions and do not move any files.
  - Notify the user with a system message (pop-up window) describing the error.
  - Direct the user to the log file for further details.
  - Log errors with timestamps and clear descriptions.
  - For CLI mode, print a concise error message to the terminal.
  - For GUI, offer a button to open the log file directly.
  - Provide actionable suggestions in the error message (e.g., “Check folder permissions”).
  - Optionally allow the user to retry the operation after fixing the issue.
  - For non-critical warnings (e.g., skipped unsupported files), log them but do not stop the whole process.
  - Example error messages:
    - "Permission denied: Unable to move 'photo1.jpg' to /Photos. Check folder access rights."
    - "Disk full: Cannot move files. Free up space and try again."
    - "Configuration error: Target folder '/Photos' does not exist."
    - "Skipped unsupported file: 'archive.zip'"
  - Error Handling Flowchart:
    1. Error detected →
    2. Stop all file operations →
    3. Log error with timestamp and details →
    4. Notify user via system message (CLI/GUI) →
    5. Suggest corrective action →
    6. User can retry or review log for details
- **Success Criteria:** (to be defined)
  - All targeted files are sorted into the correct folders according to user-defined rules.
  - No files are lost, overwritten, or corrupted during the process.
  - The user receives a clear notification using the system's default notification method (not GUI pop-ups) confirming completion.
  - A log file is generated with details of all actions taken and any warnings.
  - The app handles all expected file types and folder structures.
  - No critical errors occur; any non-critical issues are logged and reported.
  - The user can easily find and review the log file.
  - For event-driven mode, new files are sorted promptly after system notification.
  - The app’s performance is acceptable (e.g., sorting completes within a reasonable time).
  - The user can customize sorting rules and log file location.
  - The app is easy to use for both IT and non-IT users.
  - Measurable goals: Sorts 1000 files in under 1 minute; user sees "Sort complete" notification; log file contains all actions and errors.
  - Example feedback: "Sorting was fast and accurate. Log file was easy to find and understand."

## Step 1: Problem Framing

- What are the main pain points with your current workflow?
  - Example: "My Downloads folder is always cluttered and hard to find files."
- What file types and folders do you most want to organize?
  - This should be customizable by the user.
  - By default, all image file types (e.g., .jpg, .png, .gif) should be sorted into the Photos folder, or a folder of the user's choosing.
  - The same logic applies for other file types (e.g., documents, videos, music, archives) and folders.
  - Example: "I want all PDFs and images sorted into Documents and Photos folders."
- How often do you want this to run (manual, scheduled, on login)?
  - This should be set by the user.
  - On app install, the user will be able to choose (and later change in settings) whether to run Messy Desk on login, manually, or instantly (when notified by the system that activity happened in the folder).
  - Example: "I want it to run every time I log in."
- What rules should govern file sorting (by extension, date, size, etc.)?
  - Sorting will be primarily by file type, with files placed in the root of their designated folder (e.g., photo file types in the top level of the Photos folder).
  - Users can specify whether to further sort files into subfolders based on date (default YYYY-MM-DD, with options for MM-DD-YYYY or word formats like Mar 3 2024 or March 3 2024).
  - Users can also sort by name (e.g., files starting with "Belize" or photos with location data for Belize go to a "Belize Trip" folder; files containing "statement" or ending with "bills" go to user-chosen folders).
  - All sorting rules and search terms should be fully customizable by the user.
  - Example: "Sort all files with 'invoice' in the name into the Invoices folder."
- What logging and reporting features are most important?
  - By default, log every file move, rename, or deletion with timestamp, source, and destination.
  - Log all errors and warnings, including skipped files and permission issues.
  - Allow user to set log level (INFO, WARNING, ERROR, DEBUG); for the UI version, explain these levels to the user (default: INFO).
  - Store logs in the default location specified in the code, but allow the user to change this location.
  - Do not provide a summary report after each run by default, but allow the user to enable this feature if desired.
  - For event-driven mode, log the triggering event and resulting actions.
  - Allow user to view recent logs from the UI or CLI.
  - Option to email or export reports for auditing or troubleshooting.
  - Log configuration changes and user actions (e.g., rule updates).
  - Example: "I want to see a log of all files moved and any errors."
- Any security or privacy concerns (e.g., sensitive files)?
  - Allow users to exclude certain folders, file types, or file name strings (e.g., files containing specific words) from sorting. By default, everything sorts.
  - Do not log file contents, only metadata (name, type, action).
  - Ensure logs do not contain personal information or sensitive data.
  - Use secure file operations to avoid data loss or unauthorized access.
  - Provide warnings before moving large batches of files or files from protected folders.
  - Allow users to set permissions for who can run or configure the app.
  - Support encrypted log files or password-protected settings for extra privacy.
  - Never transmit files or logs outside the user’s device without explicit permission.
  - Clearly document what data is collected, stored, and how it is used.
  - Example: "Exclude my tax documents and medical files from sorting."

## Step 2: Scaffolding & Conceptual Focus

- Use `argparse` for CLI (see: https://docs.python.org/3/library/argparse.html)
- Use `pathlib` for file/folder operations (see: https://docs.python.org/3/library/pathlib.html)
- Use `logging` for diagnostics (see: https://docs.python.org/3/library/logging.html)
- Structure code for easy testing and extension
- Example code snippet for CLI:
  ```python
  import argparse
  parser = argparse.ArgumentParser(description="Sort files in Downloads and Desktop.")
  parser.add_argument('--sort', choices=['downloads', 'desktop', 'both'], default='both')
  args = parser.parse_args()
  ```

## Step 3: Implementation Prompts

- Implement environment checks (e.g., Python version, folder access)
- Implement folder scanning and sorting logic (by type, date, name)
- Implement logging and error handling (configurable log level, error messages)
- Implement CLI argument parsing (argparse)
- Estimated time: 1-2 hours per prompt

## Step 4: Code Review & Feedback

- Review for clarity, structure, error handling, and style
- Use checklist:
  - Are function and variable names descriptive?
  - Is code modular and easy to test?
  - Are errors handled explicitly and logged?
  - Is logging level appropriate?
  - Are user settings respected?
- Example feedback:
  - "Consider using pathlib for file operations."
  - "Add more descriptive error messages."

## Step 5: Model Solution

- Provide a complete, idiomatic implementation after review
- Solution outline:
  - main.py: CLI entry point, argument parsing
  - organizer.py: Sorting logic
  - config.py: Configuration management
  - preflight.py: Environment checks
  - logging setup: Logging and reporting
- Highlights:
  - Uses pathlib, argparse, logging
  - Modular, testable code
  - User-customizable rules and settings

---

## Glossary

- **Sorting rule:** A user-defined condition for organizing files (e.g., by type, date, name).
- **Event-driven:** App responds to system notifications about folder changes.
- **Metadata:** Information about a file (name, type, action) but not its contents.
- **Protected folder:** A folder the user marks as sensitive or restricted.

## Example User Story

1. User installs Messy Desk.
2. User sets up sorting rules and exclusions in the settings.
3. User runs the app manually or configures it to run on login or event.
4. App sorts files, logs actions, and notifies the user.
5. User reviews logs and adjusts rules as needed.

## High-Level Architecture

- CLI and UI frontends
- Sorting engine
- Logging/reporting module
- Configuration manager
- Event listener (for event-driven mode)

## Getting Started

1. Install Python 3.9+ and clone the repository.
2. Create and activate a virtual environment.
3. Run `python3 main.py` or launch the UI.
4. Set up your sorting rules and preferences.

## Configuration File Template

```ini
[General]
sort_on_login = true
log_level = INFO
log_file = /path/to/logfile.log

[Rules]
images = /Photos
statements = /Documents/Statements
bills = /Documents/Bills
exclude = /Secret, .env, temp
```

## Feature Mapping Table

| Feature              | Implementation Step     |
| -------------------- | ----------------------- |
| Sorting by date      | Sorting engine, config  |
| Exclusions           | Config manager, sorting |
| Logging              | Logging module          |
| Event-driven sorting | Event listener, sorting |
| UI log viewer        | UI frontend, logging    |

## Troubleshooting

- Permission errors: Check folder access rights.
- Missing folders: Verify target folders exist.
- Log not updating: Check log file path and permissions.

---

### Ideas & TODOs

- [ ] Confirm Python version and OS targets
- [ ] Define sorting rules and configuration options
- [ ] Add scheduling/automation support
- [ ] Add test suite (pytest)
- [ ] Improve documentation and usage examples
- [ ] Add support for more file types/folders
- [ ] Add logging configuration options
- [ ] Add error reporting and recovery features

---

Add new ideas and planning notes below as we discuss.

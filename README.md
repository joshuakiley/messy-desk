# Messy Desk

A command-line utility to automatically organize files on your desktop and in your downloads folder.

## Features

- Sorts files based on user-defined rules (in development).
- Targets the Downloads folder, Desktop folder, or both.
- Robust logging to both the console and a file.
- Configurable via command-line arguments.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone [https://github.com/your-username/messy-desk.git](https://github.com/your-username/messy-desk.git)
   cd messy-desk
   ```

2. This project currently uses only the Python standard library. If external dependencies are added in the future, they will be listed in a `requirements.txt` file.

## Configuration

Before running the application, you must set the following environment variable. This tells the application which environment it's running in (e.g., `development` or `production`).

- **For macOS/Linux:**

  ```bash
  export APP_ENV=development
  ```

- **For Windows (Command Prompt):**

  ```cmd
  set APP_ENV=development
  ```

## Usage

You can run the application from the root of the project directory.

- **To sort both the desktop and downloads folders with default settings:**

  ```bash
  python3 main.py
  ```

- **To sort only the downloads folder:**

  ```bash
  python3 main.py --sort downloads
  ```

- **To specify a custom path for the log file:**

  ```bash
  python3 main.py --log-file /path/to/your/custom.log
  ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

# Messy Desk

A command-line utility to automatically organize files on your desktop and in your downloads folder.

## Features

- Sorts files based on user-defined rules (in development).
- Targets the Downloads folder, Desktop folder, or both.
- Robust logging to both the console and a file.
- Configurable via command-line arguments.

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine and navigate into the directory:

   ```bash
   git clone [https://github.com/your-username/messy-desk.git](https://github.com/your-username/messy-desk.git)
   cd messy-desk
   ```

2. **Create and Activate a Virtual Environment**

   Using a virtual environment is a crucial best practice for isolating project dependencies.

   - **Create the environment:**

     ```bash
     python3 -m venv venv
     ```

   - **Activate the environment:**
     _**On macOS & Linux:**
     `bash
  source venv/bin/activate
  `
     _ **On Windows:**
     `cmd
  venv\Scripts\activate
  `
     You'll know the environment is active when your terminal prompt is prefixed with `(venv)`.

3. **Install Dependencies**

   This project currently uses only the Python standard library. If external dependencies were added in the future, you would install them using `pip` like this:

   ```bash
   pip install -r requirements.txt
   ```

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

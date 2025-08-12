"""
This is the preflight module of the application.
It performs checks and validations before the main execution.
"""

import os


def check_environment() -> None:
    """Checks if required environment variables are set.

    Raises:
        EnvironmentError: If a required variable is not set.
    """
    if not os.getenv("APP_ENV"):
        raise EnvironmentError("APP_ENV is not set.")

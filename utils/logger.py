import logging
import os

class Logger:
    """
    A simple logging utility class to manage logging to a file.

    This class initializes a logging setup that logs messages to a file 
    in the 'logs' directory. If the directory does not exist, it will be created. 
    The logs are recorded with timestamps, log levels, and log messages.

    Methods:
        log_info(message: str): Logs an informational message.
        log_warning(message: str): Logs a warning message.
        log_error(message: str): Logs an error message.
    """

    def __init__(self, log_file="application.log"):
        """
        Initializes the Logger instance and sets up logging to a file.

        Args:
            log_file (str): The name of the log file where logs will be stored. 
                             Defaults to "application.log".
                             
        Logs:
            - If the 'logs' directory doesn't exist, it will be created.
            - Initializes the logging configuration with INFO level logging.
            - Logs messages to both a file and, optionally, to the console.

        Example:
            logger = Logger()
            logger.log_info("Application started")
        """
        # Create a logs folder if it doesn't exist
        if not os.path.exists("logs"):
            os.makedirs("logs")
        
        log_file_path = os.path.join("logs", log_file)

        # Set up basic configuration for logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file_path),
                # logging.StreamHandler()  # Uncomment if you want to log to the console as well
            ]
        )

        logging.info("Logger initialized successfully with log file: %s", log_file_path)

    @staticmethod
    def log_info(message):
        """
        Logs an informational message.

        Args:
            message (str): The message to log.

        Example:
            Logger.log_info("This is an info message.")
        """
        logging.info(message)
        logging.debug("Info message logged: %s", message)

    @staticmethod
    def log_warning(message):
        """
        Logs a warning message.

        Args:
            message (str): The message to log.

        Example:
            Logger.log_warning("This is a warning message.")
        """
        logging.warning(message)
        logging.debug("Warning message logged: %s", message)

    @staticmethod
    def log_error(message):
        """
        Logs an error message.

        Args:
            message (str): The message to log.

        Example:
            Logger.log_error("This is an error message.")
        """
        logging.error(message)
        logging.debug("Error message logged: %s", message)

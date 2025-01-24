import logging
import sys

# Logging formatter supporting colorized output
class LogFormatter(logging.Formatter):

    COLOR_CODES = {
        logging.CRITICAL: "\033[1;35m", # bright/bold magenta
        logging.ERROR:    "\033[1;31m", # bright/bold red
        logging.WARNING:  "\033[1;33m", # bright/bold yellow
        logging.INFO:     "\033[0;37m", # white / light gray
        logging.DEBUG:    "\033[1;30m"  # bright/bold dark gray
    }

    RESET_CODE = "\033[0m"

    def __init__(self, *args, **kwargs):
        super(LogFormatter, self).__init__(*args, **kwargs)
        # Define date format here
        self.datefmt = "%Y-%m-%d %H:%M:%S"

    def format(self, record):
        log_message = super().format(record)
        if record.levelno in self.COLOR_CODES:
            color_on = self.COLOR_CODES[record.levelno]
            color_off = self.RESET_CODE
            return f"{color_on}{log_message}{color_off}"
        return log_message


def get_logger(logger_name="default", console_log_output="stdout", console_log_level="INFO", logfile_file="automation.log", logfile_log_level="DEBUG"):
    """
    Set up a logger with the specified name and configurations.
    :param logger_name: Name of the logger.
    :param console_log_output: Output stream for console logging ('stdout' or 'stderr').
    :param console_log_level: Logging level for console output.
    :param logfile_file: File path for log file.
    :param logfile_log_level: Logging level for log file.
    :return: Configured logger instance.
    """
    # Create logger instance with a specific name
    logger = logging.getLogger(logger_name)

    # Clear existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Set the default log level to DEBUG
    logger.setLevel(logging.DEBUG)

    # Console handler setup
    console_log_output = console_log_output.lower()
    if console_log_output == "stdout":
        console_log_output = sys.stdout
    elif console_log_output == "stderr":
        console_log_output = sys.stderr
    else:
        print(f"Failed to set console output: invalid output: '{console_log_output}'")
        return None
    console_handler = logging.StreamHandler(console_log_output)

    try:
        console_handler.setLevel(console_log_level.upper())  # Set console log level
    except ValueError:
        print(f"Failed to set console log level: invalid level: '{console_log_level}'")
        return None

    # Formatter for console
    console_formatter = LogFormatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler setup
    try:
        logfile_handler = logging.FileHandler(logfile_file)
    except Exception as e:
        print(f"Failed to set up log file: {str(e)}")
        return None

    try:
        logfile_handler.setLevel(logfile_log_level.upper())  # Set log file log level
    except ValueError:
        print(f"Failed to set log file log level: invalid level: '{logfile_log_level}'")
        return None

    # Formatter for log file
    logfile_formatter = LogFormatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logfile_handler.setFormatter(logfile_formatter)
    logger.addHandler(logfile_handler)

    return logger

import sys

from loguru import logger

_LEVEL_ABBREVIATIONS = {
    "TRACE": "TRC",
    "DEBUG": "DBG",
    "INFO": "INF",
    "SUCCESS": "SUC",
    "WARNING": "WRN",
    "ERROR": "ERR",
    "CRITICAL": "CRT",
}


def _compact_log_format(record):
    """Return the compact format for a Loguru record."""
    level_name = record["level"].name
    level = _LEVEL_ABBREVIATIONS.get(level_name, level_name[:3].upper())
    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green>"
        f" | <level>{level}</level>"
        " | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
        " | <level>{message}</level>\n{exception}"
    )


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO, configurable via env var)
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)
    """
    import os

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level, format=_compact_log_format)
    logger.add(
        log_file,
        level="DEBUG",
        format=_compact_log_format,
        rotation="50 KB",
        retention=1,
    )


@logger.catch
def main():
    """Run the application.

    Configures logging and prints a greeting to verify the setup works.
    """
    configure_logging()
    logger.info("Hello from secondbrain!")

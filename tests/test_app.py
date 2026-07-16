import re
from types import SimpleNamespace

import pytest
from loguru import logger

from secondbrain.app import compact_log_format, configure_logging, main

LOG_LINE = re.compile(
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    r" \| (?P<level>[A-Z]{3})"
    r" \| secondbrain\.app:main:\d+"
    r" \| Hello from secondbrain!$"
)


def test_main_uses_compact_format_for_console_and_file(capfd, _test_log_file):
    main()
    captured = capfd.readouterr()

    console_log = captured.err.strip()
    file_log = _test_log_file.read_text().strip()
    console_match = LOG_LINE.fullmatch(console_log)

    assert console_match is not None
    assert console_match["level"] == "INF"
    assert file_log == console_log


@pytest.mark.parametrize(
    ("log_method", "abbreviation"),
    [
        (logger.debug, "DBG"),
        (logger.info, "INF"),
        (logger.warning, "WRN"),
        (logger.error, "ERR"),
    ],
)
def test_log_levels_use_short_labels(capfd, log_method, abbreviation):
    configure_logging()

    log_method("level abbreviation")

    assert f" | {abbreviation} | " in capfd.readouterr().err


@pytest.mark.parametrize(
    ("level_name", "abbreviation"),
    [
        ("TRACE", "TRC"),
        ("SUCCESS", "SUC"),
        ("CRITICAL", "CRT"),
        ("VERBOSE", "VER"),
    ],
)
def test_other_log_levels_use_conventional_or_fallback_labels(level_name, abbreviation):
    record = {"level": SimpleNamespace(name=level_name)}

    assert f" | <level>{abbreviation}</level>" in compact_log_format(record)

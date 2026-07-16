"""Shared test fixtures."""

import pytest


@pytest.fixture(autouse=True)
def _test_log_file(tmp_path, monkeypatch):
    log_file = tmp_path / "test.log"
    monkeypatch.setenv("LOG_FILE", str(log_file))
    return log_file

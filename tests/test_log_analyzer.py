"""Tests for `log_analyzer` package."""

from pathlib import Path

from log_analyzer.utils import calculate_metrics, read_file_log


def test_calculate_metrics():
    """Проверяет, что calculate_metrics правильно считает метрики."""
    times = [0.1, 0.2, 0.3, 0.4, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
    result = calculate_metrics(times)

    assert result["count"] == 10
    assert result["mean"] == sum(times) / 10
    assert result["median"] == (0.5 + 1.0) / 2
    assert result["perc_95"] == 5.0
    assert result["min"] == 0.1
    assert result["max"] == 5.0


def test_read_file_log_list():
    """Проверяем, что функция возвращает весь список логов из файла по-умолчанию."""
    test_dir = Path(__file__).parent
    log_path = test_dir / "pu.txt"
    result = read_file_log(str(log_path))
    assert len(result) == 40


def test_read_file_log_set():
    """Проверяем, что функция возвращает уникальное множество логов из файла, с флагом True."""
    test_dir = Path(__file__).parent
    log_path = test_dir / "pu.txt"
    result = read_file_log(str(log_path), True)
    assert len(result) == 39
    assert isinstance(result, set)

"""Tests for `log_analyzer` package."""

from log_analyzer.utils import calculate_metrics


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

from log_analyzer.analyzer import LogAnalyzer


def test_parse_log_file():
    # Создаём экземпляр с пустым конфигом
    config = {
        "REPORT_SIZE": 5,
        "LOG_DIR": "dummy",
        "LOG_PATTERN": r".*",
    }
    analyzer = LogAnalyzer(config)

    # Подменяем _lines тестовыми данными
    analyzer._lines = [
        '1.140.178.176 - - [29/Jun/2017:08:13:51 +0300] "GET /test HTTP/1.1" 200 22 "-" "-" "-" "-" "-" 0.123',
        '1.140.178.176 - - [29/Jun/2017:08:13:52 +0300] "GET /test2 HTTP/1.1" 200 22 "-" "-" "-" "-" "-" 0.456',
        "битая строка без времени",
        '1.140.178.176 - - [29/Jun/2017:08:13:53 +0300] "GET /test3 HTTP/1.1" 200 22 "-" "-" "-" "-" "-" нечисло',
    ]
    analyzer._times = []  # очищаем перед вызовом

    # Вызываем тестируемый метод
    analyzer._parse_log_file()

    # Проверяем результат
    assert analyzer._times == [0.123, 0.456]
    assert len(analyzer._times) == 2

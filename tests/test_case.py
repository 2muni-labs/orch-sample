import pytest

from orch_sample.case import camel_case, snake_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello_world"),
        ("helloWorld", "hello_world"),
        ("HelloWorld", "hello_world"),
        ("HTTPServer error", "http_server_error"),
        ("parseJSON2Data", "parse_json_2_data"),
        ("already_snake_case", "already_snake_case"),
        ("kebab-case-text", "kebab_case_text"),
        ("café menu", "caf_menu"),
        ("  --  ", ""),
        ("", ""),
    ],
)
def test_snake_case(text: str, expected: str) -> None:
    assert snake_case(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", "helloWorld"),
        ("Hello World", "helloWorld"),
        ("HTTP server", "httpServer"),
        ("snake_case_text", "snakeCaseText"),
        ("version 2 beta", "version2Beta"),
        ("XMLHttpRequest", "xmlHttpRequest"),
        ("ALL CAPS", "allCaps"),
        ("...", ""),
        ("", ""),
    ],
)
def test_camel_case(text: str, expected: str) -> None:
    assert camel_case(text) == expected

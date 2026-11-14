import pytest

from orch_sample.slug import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello, World!", "hello-world"),
        ("  leading and trailing  ", "leading-and-trailing"),
        ("Crème brûlée", "creme-brulee"),
        ("a--b__c", "a-b-c"),
        ("", ""),
        ("!!!", ""),
    ],
)
def test_slugify(text: str, expected: str) -> None:
    assert slugify(text) == expected


def test_a_custom_separator_is_used_and_stripped() -> None:
    assert slugify("_Hello World_", separator="_") == "hello_world"


def test_an_empty_separator_is_refused() -> None:
    with pytest.raises(ValueError):
        slugify("x", separator="")

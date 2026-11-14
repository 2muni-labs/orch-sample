import pytest

from orch_sample.truncate import truncate


@pytest.mark.parametrize(
    ("text", "width", "expected"),
    [
        ("The quick brown fox", 19, "The quick brown fox"),
        ("The quick brown fox", 30, "The quick brown fox"),
        ("The quick brown fox", 15, "The quick..."),
        ("The quick brown fox", 12, "The quick..."),
        ("The quick brown fox", 11, "The..."),
        ("a b c d", 5, "a..."),
        ("one\ntwo three", 8, "one..."),
        ("Supercalifragilistic", 10, "..."),
        ("", 0, ""),
        ("ab", 2, "ab"),
    ],
)
def test_truncate(text: str, width: int, expected: str) -> None:
    assert truncate(text, width) == expected


def test_a_custom_placeholder_counts_toward_width() -> None:
    assert truncate("Hello world", 8, placeholder="…") == "Hello…"


def test_an_empty_placeholder_cuts_at_the_word_end() -> None:
    assert truncate("Hello world", 8, placeholder="") == "Hello"


def test_a_result_never_exceeds_width() -> None:
    text = "lorem ipsum dolor sit amet consectetur"
    for width in range(3, len(text) + 1):
        assert len(truncate(text, width)) <= width


def test_a_negative_width_is_refused() -> None:
    with pytest.raises(ValueError):
        truncate("abc", -1)


def test_a_placeholder_longer_than_width_is_refused_when_cutting() -> None:
    with pytest.raises(ValueError):
        truncate("abc def", 2)

import pytest

from orch_sample.wrap import wrap


@pytest.mark.parametrize(
    ("text", "width", "expected"),
    [
        ("The quick brown fox", 10, ["The quick", "brown fox"]),
        ("The quick brown fox", 9, ["The quick", "brown fox"]),
        ("The quick brown fox", 8, ["The", "quick", "brown", "fox"]),
        ("The quick brown fox", 19, ["The quick brown fox"]),
        ("The quick brown fox", 100, ["The quick brown fox"]),
        ("a  b\nc", 3, ["a b", "c"]),
        ("  leading and trailing  ", 7, ["leading", "and", "trailing"]),
        ("Supercalifragilistic is long", 5, ["Supercalifragilistic", "is", "long"]),
        ("a b c d e", 1, ["a", "b", "c", "d", "e"]),
        ("a b c d e", 3, ["a b", "c d", "e"]),
    ],
)
def test_wrap(text: str, width: int, expected: list[str]) -> None:
    assert wrap(text, width) == expected


@pytest.mark.parametrize("text", ["", "   ", "\n\t"])
def test_text_without_words_gives_no_lines(text: str) -> None:
    assert wrap(text, 5) == []


@pytest.mark.parametrize("width", [0, -1])
def test_a_width_below_one_is_rejected(width: int) -> None:
    with pytest.raises(ValueError):
        wrap("a b", width)

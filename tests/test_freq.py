import pytest

from orch_sample.freq import word_frequencies

TEXT = "It's a dog's life. A DOG'S life!"


def test_words_are_counted_without_case() -> None:
    assert word_frequencies(TEXT) == [
        ("a", 2),
        ("dog's", 2),
        ("life", 2),
        ("it's", 1),
    ]


def test_ties_keep_the_order_of_first_occurrence() -> None:
    assert word_frequencies("b a c a b c d") == [
        ("b", 2),
        ("a", 2),
        ("c", 2),
        ("d", 1),
    ]


def test_more_frequent_words_come_first() -> None:
    assert word_frequencies("x y y z z z") == [("z", 3), ("y", 2), ("x", 1)]


def test_top_limits_the_result() -> None:
    assert word_frequencies(TEXT, top=2) == [("a", 2), ("dog's", 2)]


def test_top_larger_than_the_result_returns_everything() -> None:
    assert word_frequencies("one two", top=10) == [("one", 1), ("two", 1)]


def test_top_zero_returns_nothing() -> None:
    assert word_frequencies(TEXT, top=0) == []


def test_an_empty_text_has_no_frequencies() -> None:
    assert word_frequencies("") == []


def test_a_negative_top_is_refused() -> None:
    with pytest.raises(ValueError):
        word_frequencies(TEXT, top=-1)

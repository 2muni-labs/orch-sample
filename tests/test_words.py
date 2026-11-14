from orch_sample.words import word_count, words


def test_words_keep_inner_apostrophes() -> None:
    assert words("It's a dog's life.") == ["It's", "a", "dog's", "life"]


def test_word_count_ignores_punctuation_and_spaces() -> None:
    assert word_count("  one, two;  three...  ") == 3


def test_an_empty_text_has_no_words() -> None:
    assert word_count("") == 0

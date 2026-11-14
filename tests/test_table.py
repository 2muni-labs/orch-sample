import pytest

from orch_sample.table import format_table


def test_the_spec_example() -> None:
    assert (
        format_table(["a", "bb"], [["xyz", "1"]], align="lr")
        == "a   | bb\n----+---\nxyz |  1"
    )


def test_columns_are_left_aligned_by_default() -> None:
    assert format_table(["name", "n"], [["ab", "10"], ["c", "7"]]) == (
        "name | n\n-----+---\nab   | 10\nc    | 7"
    )


def test_right_alignment_pads_on_the_left() -> None:
    assert format_table(["n"], [["1"], ["100"]], align="r") == ("  n\n---\n  1\n100")


def test_center_puts_the_extra_space_on_the_right() -> None:
    assert format_table(["abcde", "x"], [["a", "y"], ["ab", "z"]], align="cl") == (
        "abcde | x\n------+--\n  a   | y\n ab   | z"
    )


def test_a_header_wider_than_its_cells_sets_the_width() -> None:
    assert format_table(["long header"], [["a"]], align="r") == (
        "long header\n-----------\n          a"
    )


def test_trailing_spaces_are_removed_from_each_line() -> None:
    text = format_table(["a", "b"], [["x", ""], ["y", "zz"]])
    assert text == "a | b\n--+---\nx |\ny | zz"
    assert all(line == line.rstrip(" ") for line in text.split("\n"))


def test_no_rows_gives_the_header_and_separator() -> None:
    assert format_table(["a", "bb"], []) == "a | bb\n--+---"


def test_empty_cells_are_allowed() -> None:
    assert format_table(["", "b"], [["", ""]], align="rr") == (" | b\n-+--\n |")


def test_there_is_no_trailing_newline() -> None:
    assert not format_table(["a"], [["b"]]).endswith("\n")


@pytest.mark.parametrize(
    ("headers", "rows", "align"),
    [
        ([], [], None),
        (["a", "b"], [["x"]], None),
        (["a"], [["x", "y"]], None),
        (["a\nb"], [], None),
        (["a"], [["x\ny"]], None),
        (["a", "b"], [], "l"),
        (["a", "b"], [], "lrc"),
        (["a"], [], "x"),
        (["a"], [], "L"),
    ],
)
def test_invalid_input_is_rejected(
    headers: list[str], rows: list[list[str]], align: str | None
) -> None:
    with pytest.raises(ValueError):
        format_table(headers, rows, align)

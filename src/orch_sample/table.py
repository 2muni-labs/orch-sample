"""Format rows as an aligned plain-text table."""


def format_table(
    headers: list[str], rows: list[list[str]], align: str | None = None
) -> str:
    """Return headers and rows as a table with one alignment per column."""
    if not headers:
        raise ValueError("Headers must not be empty")
    column_count = len(headers)
    if any(len(row) != column_count for row in rows):
        raise ValueError("Each row must have one cell per header")
    all_rows = [headers, *rows]
    if any("\n" in cell for row in all_rows for cell in row):
        raise ValueError("Headers and cells must not contain newlines")
    if align is None:
        align = "l" * column_count
    if len(align) != column_count or any(mode not in "lrc" for mode in align):
        raise ValueError("Alignment must contain one of l, r, or c per column")

    widths = [max(len(row[index]) for row in all_rows) for index in range(column_count)]

    def format_row(row: list[str]) -> str:
        cells = []
        for cell, width, mode in zip(row, widths, align, strict=True):
            padding = width - len(cell)
            left = padding if mode == "r" else padding // 2 if mode == "c" else 0
            cells.append(" " * left + cell + " " * (padding - left))
        return " | ".join(cells).rstrip(" ")

    separator = "-+-".join("-" * width for width in widths)
    return "\n".join(
        [format_row(headers), separator, *(format_row(row) for row in rows)]
    )

"""Shorten text at word boundaries."""


def truncate(text: str, width: int, placeholder: str = "...") -> str:
    """Return text cut at a word end so that it fits in width with placeholder."""
    if width < 0:
        raise ValueError("width must be non-negative")
    if len(text) <= width:
        return text
    if len(placeholder) > width:
        raise ValueError("placeholder must fit within width")

    limit = width - len(placeholder)
    for i in range(limit, 0, -1):
        if not text[i - 1].isspace() and text[i].isspace():
            return text[:i] + placeholder
    return placeholder

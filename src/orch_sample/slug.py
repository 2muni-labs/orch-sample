"""Turn free text into URL slugs."""

import re
import unicodedata

_NON_WORD = re.compile(r"[^a-z0-9]+")


def slugify(text: str, separator: str = "-") -> str:
    """Return a lowercase ASCII slug of text, words joined by separator.

    Accents are dropped, every run of other characters becomes one separator,
    and separators at either end are removed.
    """
    if not separator:
        raise ValueError("separator must not be empty")
    ascii_text = (
        unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    )
    return _NON_WORD.sub(separator, ascii_text.lower()).strip(separator)

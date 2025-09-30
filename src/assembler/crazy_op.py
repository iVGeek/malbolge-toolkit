from .crazy_table import crz as table_crz


def crazy_transform(a: int, b: int) -> int:
    """Compatibility wrapper that uses the table-based crz implementation."""
    return table_crz(a, b)


def crz(a: int, b: int) -> int:
    """Direct table lookup alias."""
    return table_crz(a, b)

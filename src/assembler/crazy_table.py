"""Generate a deterministic 256x256 'crazy' operation table.

This implementation creates a reproducible table using a mix of bitwise
and arithmetic transforms. It is an experimental replacement for the
real Malbolge crz table which is historically defined by the language
specification. The table here is chosen to be deterministic and
invertible enough for educational self-modifying behavior in the VM.
"""

from typing import List


def make_table() -> List[List[int]]:
    table = [[0] * 256 for _ in range(256)]
    for a in range(256):
        for b in range(256):
            # deterministic mix: rotate a by (b % 8), XOR with (b rotated by 3), add index
            rot_a = ((a << (b & 7)) | (a >> (8 - (b & 7)))) & 0xFF
            rot_b = ((b << 3) | (b >> 5)) & 0xFF
            val = (rot_a ^ rot_b ^ ((a + b) & 0xFF)) & 0xFF
            table[a][b] = val
    return table

# Pre-generate at import time for speed
CRAZY_TABLE = make_table()


def crz(a: int, b: int) -> int:
    return CRAZY_TABLE[a & 0xFF][b & 0xFF]

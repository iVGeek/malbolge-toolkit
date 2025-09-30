# Experimental implementation of Malbolge 'crazy' operation.
# This is a simplified deterministic mapping that mimics the idea of a table-based transform.

# A real Malbolge implementation uses a 256x256 lookup table; here we provide a small
# pseudo-crazy table generated from bitwise operations for educational purposes.

def crazy_transform(a: int, b: int) -> int:
    # Keep inputs in byte range
    a &= 0xFF
    b &= 0xFF
    # Example transform: mix bits of a and b with rotations and XORs
    x = ((a << 3) | (a >> 5)) & 0xFF
    y = ((b << 5) | (b >> 3)) & 0xFF
    return (x ^ y ^ ((a + b) & 0xFF)) & 0xFF

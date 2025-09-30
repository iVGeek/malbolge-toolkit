def dump_memory(mem, width=16):
    """Return a hex dump string of memory (bytes or ints)"""
    if isinstance(mem, bytes):
        mem = list(mem)
    lines = []
    for i in range(0, len(mem), width):
        chunk = mem[i:i+width]
        hexs = ' '.join(f"{b:02x}" for b in chunk)
        lines.append(f"{i:08x}: {hexs}")
    return '\n'.join(lines)

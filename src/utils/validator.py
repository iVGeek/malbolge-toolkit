def validate_source(source):
    """Basic validation for simple Malbolge-like source (checks tokens)"""
    lines = [l.split('#')[0].strip() for l in source.split('\n')]
    for lineno, line in enumerate(lines, start=1):
        if not line:
            continue
        parts = line.split()
        # allow labels ending with ':'
        if parts[0].endswith(':'):
            continue
        # allow numeric literals
        if parts[0].isdigit():
            continue
        # allow a small set of mnemonics
        allowed = {'jmp','out','in','rot','mov','add','cra','nop','hlt'}
        if parts[0].lower() not in allowed:
            raise ValueError(f"Unknown token on line {lineno}: {parts[0]}")
    return True



####return ()
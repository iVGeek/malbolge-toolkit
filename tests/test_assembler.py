import io
from src.assembler.malbolge_asm import MalbolgeAssembler


def test_assemble_simple():
    asm = MalbolgeAssembler()
    src = """
    1
    2
    out
    """
    b = asm.assemble(src)
    assert isinstance(b, (bytes, bytearray))
    assert len(b) == 3

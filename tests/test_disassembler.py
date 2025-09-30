from src.disassembler.malbolge_disasm import MalbolgeDisassembler


def test_disassemble_empty():
    d = MalbolgeDisassembler()
    assert d.disassemble(b'') == ''

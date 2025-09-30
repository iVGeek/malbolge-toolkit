from src.assembler.malbolge_asm import MalbolgeAssembler


def test_hello_assemble():
    asm = MalbolgeAssembler()
    with open('src/examples/hello_world.mal', 'r', encoding='utf-8') as f:
        src = f.read()
    b = asm.assemble(src)
    assert len(b) > 0

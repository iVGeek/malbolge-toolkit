from src.assembler.malbolge_asm import MalbolgeAssembler
from src.vm.full_malbolge_vm import FullMalbolgeVM


def test_assemble_and_run_emit_A():
    asm = MalbolgeAssembler()
    with open('src/examples/emit_A.mal', 'r', encoding='utf-8') as f:
        src = f.read()
    raw = asm.assemble(src, raw=True)
    vm = FullMalbolgeVM()
    vm.load(raw)
    out = vm.run()
    assert out == b'A'

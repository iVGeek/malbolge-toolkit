from src.assembler.malbolge_asm import MalbolgeAssembler
asm = MalbolgeAssembler()
src = open('src/examples/emit_A.mal','r',encoding='utf-8').read()
raw = asm.assemble(src, raw=True)
open('tests/fixtures/emit_A_raw.bin','wb').write(raw)
print('wrote', len(raw), 'bytes')



###return ()
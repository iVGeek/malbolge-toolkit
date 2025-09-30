# Release Notes v0.1.0

This release creates the Malbolge Development Toolkit (MDT) — an educational
framework for assembling, disassembling, debugging, and running simplified
Malbolge-like programs.

Highlights
- Assembler: `src/assembler/malbolge_asm.py` — assemble human-readable Malbolge-like source to binary.
- Disassembler: `src/disassembler/malbolge_disasm.py` — simple binary disassembly.
- VMs:
  - `src/vm/malbolge_vm.py` (SimpleMalbolgeVM) — minimal runner for quick experiments.
  - `src/vm/full_malbolge_vm.py` (FullMalbolgeVM) — more featureful VM with registers and self-modifying writes.
- Crazy operation:
  - `src/assembler/crazy_table.py` — deterministic 256x256 experimental table (CRAZY_TABLE) and `crz()` lookup.
  - `src/assembler/crazy_op.py` — compatibility wrappers.
- CI: GitHub Actions workflow to run pytest on push and PR.
- Tests: unit tests and end-to-end example demonstrate assemble->run workflow.

Notes
- The CRAZY_TABLE here is experimental and deterministic for educational use. It may not match canonical Malbolge semantics.
- This project is intentionally simplified; future work could implement canonical Malbolge behavior.

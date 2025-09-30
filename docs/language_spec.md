# Malbolge Language Specification

## Overview
Malbolge is an esoteric programming language invented by Ben Olmstead in 1998. It was designed to be intentionally difficult.

## Memory Model
- 59049 words of memory (3^10) - conceptual reference
- Each word is 10 trits (ternary digits)
- Memory is cyclic

## Instruction Set
Malbolge uses a set of instructions and a complex mapping; this document provides a simplified conceptual view used by this toolkit.

## Execution Model
- Self-modifying code
- Instructions are transformed during execution
- This toolkit provides conceptual assembler/disassembler/debugger for learning and experimentation

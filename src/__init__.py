"""
Malbolge Development Toolkit - Tools for working with the world's most difficult programming language
"""

import sys
import argparse
from .assembler.malbolge_asm import MalbolgeAssembler
from .disassembler.malbolge_disasm import MalbolgeDisassembler
from .debugger.malbolge_debug import MalbolgeDebugger
from .vm.malbolge_vm import SimpleMalbolgeVM


def main():
    parser = argparse.ArgumentParser(description='Malbolge Development Toolkit')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Assembler command
    asm_parser = subparsers.add_parser('assemble', help='Assemble Malbolge source')
    asm_parser.add_argument('input', help='Input source file')
    asm_parser.add_argument('-o', '--output', help='Output file')
    
    # Disassembler command  
    disasm_parser = subparsers.add_parser('disassemble', help='Disassemble Malbolge binary')
    disasm_parser.add_argument('input', help='Input binary file')
    
    # Debug command
    debug_parser = subparsers.add_parser('debug', help='Debug Malbolge program')
    debug_parser.add_argument('program', help='Program to debug')
    
    # Run command
    run_parser = subparsers.add_parser('run', help='Run Malbolge program')
    run_parser.add_argument('program', help='Program to run')
    
    args = parser.parse_args()
    
    if args.command == 'assemble':
        assembler = MalbolgeAssembler()
        assembler.assemble_file(args.input, args.output)
    elif args.command == 'disassemble':
        disassembler = MalbolgeDisassembler()
        print(disassembler.disassemble_file(args.input))
    elif args.command == 'debug':
        debugger = MalbolgeDebugger()
        debugger.load_program(args.program)
        debugger.run()
    elif args.command == 'run':
        # Simple execution
        with open(args.program, 'rb') as f:
            program = f.read()
        vm = SimpleMalbolgeVM()
        vm.load(program)
        out = vm.run()
        if out:
            try:
                print(out.decode('utf-8', errors='replace'))
            except Exception:
                print(out)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

import struct
from .ternary_encoder import TernaryEncoder
from .crazy_table import crz


class MalbolgeAssembler:
    """Assembles human-readable Malbolge code into binary format

    This assembler intentionally implements a simplified, educational
    subset of Malbolge-like behavior. It supports emitting either raw
    opcodes (no transformation) or the "crazy" transformed bytes.
    """

    # Malbolge instruction set (simplified representation)
    INSTRUCTIONS = {
        'jmp': 4,    # Jump
        'out': 5,    # Output
        'in': 23,    # Input
        'rot': 39,   # Rotate
        'mov': 40,   # Move
        'add': 62,   # Add
        'cra': 68,   # Crazy operation
        'nop': 81,   # No operation
        'hlt': 239,  # Halt
    }

    def __init__(self):
        self.encoder = TernaryEncoder()
        self.labels = {}
        self.program = []

    def assemble_file(self, input_file, output_file=None, raw=False):
        """Assemble a Malbolge source file

        raw=True will write raw opcodes (no crazy transform). By default the
        assembler writes transformed bytes.
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            source = f.read()

        binary = self.assemble(source, raw=raw)

        if output_file is None:
            output_file = input_file.replace('.mal', '.malb')

        with open(output_file, 'wb') as f:
            f.write(binary)

        print(f"Assembled {input_file} -> {output_file}")
        return binary

    def assemble(self, source, raw=False):
        """Assemble Malbolge source code

        If raw=True, return raw opcode bytes (no crazy transform). Otherwise
        return transformed bytes.
        """
        lines = self.preprocess(source)

        # First pass: collect labels
        self.collect_labels(lines)

        # Second pass: generate code list (integers)
        machine_code = self.generate_code(lines)

        if raw:
            return bytes([w & 0xFF for w in machine_code])
        return self.encode_program(machine_code)

    def preprocess(self, source):
        """Remove comments and empty lines"""
        lines = []
        for line in source.split('\n'):
            # Remove comments
            if '#' in line:
                line = line.split('#')[0]
            line = line.strip()
            if line:
                lines.append(line)
        return lines

    def collect_labels(self, lines):
        """First pass - collect label definitions"""
        self.labels = {}
        address = 0

        for line in lines:
            if line.endswith(':'):
                # Label definition
                label = line[:-1]
                self.labels[label] = address
            else:
                # Count words on the line as separate memory words
                parts = line.split()
                address += len(parts)

    def generate_code(self, lines):
        """Second pass - generate machine code (list of integers)"""
        program = []

        for line in lines:
            if line.endswith(':'):
                continue  # Skip label definitions

            parts = line.split()
            if not parts:
                continue

            instruction = parts[0].lower()

            if instruction in self.INSTRUCTIONS:
                opcode = self.INSTRUCTIONS[instruction]
                program.append(opcode)
                # If the instruction has an operand, append it as the next word
                if len(parts) > 1:
                    operand = parts[1]
                    if operand.isdigit():
                        program.append(int(operand) & 0xFF)
                    elif operand in self.labels:
                        program.append(self.labels[operand] & 0xFF)
                    else:
                        raise ValueError(f"Unknown operand for {instruction}: {operand}")
            elif parts[0].isdigit():
                # Direct value
                program.append(int(parts[0]) & 0xFF)
            elif parts[0] in self.labels:
                program.append(self.labels[parts[0]] & 0xFF)
            else:
                raise ValueError(f"Unknown instruction or label: {instruction}")

        return program

    def encode_program(self, program):
        """Encode program using Malbolge's crazy operation"""
        encoded = bytearray()
        for i, instruction in enumerate(program):
            encoded_byte = crz(instruction, i)
            encoded.append(encoded_byte)
        return bytes(encoded)

    def crazy_operation(self, a, b):
        """Legacy placeholder for the crazy operation"""
        return (a + b) % 256

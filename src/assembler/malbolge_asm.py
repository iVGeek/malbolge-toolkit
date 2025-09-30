import struct
from .ternary_encoder import TernaryEncoder

class MalbolgeAssembler:
    """Assembles human-readable Malbolge code into binary format"""
    
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
        
    def assemble_file(self, input_file, output_file=None):
        """Assemble a Malbolge source file"""
        with open(input_file, 'r', encoding='utf-8') as f:
            source = f.read()
            
        binary = self.assemble(source)
        
        if output_file is None:
            output_file = input_file.replace('.mal', '.malb')
            
        with open(output_file, 'wb') as f:
            f.write(binary)
            
        print(f"Assembled {input_file} -> {output_file}")
        return binary
    
    def assemble(self, source):
        """Assemble Malbolge source code"""
        lines = self.preprocess(source)
        
        # First pass: collect labels
        self.collect_labels(lines)
        
        # Second pass: generate code
        machine_code = self.generate_code(lines)
        
        return machine_code
    
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
                address += 1
    
    def generate_code(self, lines):
        """Second pass - generate machine code"""
        self.program = []
        address = 0
        
        for line in lines:
            if line.endswith(':'):
                continue  # Skip label definitions
                
            parts = line.split()
            if not parts:
                continue
                
            instruction = parts[0].lower()
            
            if instruction in self.INSTRUCTIONS:
                # Regular instruction
                opcode = self.INSTRUCTIONS[instruction]
                self.program.append(opcode)
            elif instruction.isdigit():
                # Direct value
                self.program.append(int(instruction))
            elif instruction in self.labels:
                # Label reference
                self.program.append(self.labels[instruction])
            else:
                raise ValueError(f"Unknown instruction or label: {instruction}")
                
            address += 1
            
        # Convert to Malbolge's crazy encoding
        return self.encode_program(self.program)
    
    def encode_program(self, program):
        """Encode program using Malbolge's crazy operation"""
        encoded = bytearray()
        
        for i, instruction in enumerate(program):
            # Apply Malbolge's encoding rules
            encoded_byte = self.crazy_operation(instruction, i)
            encoded.append(encoded_byte)
            
        return bytes(encoded)
    
    def crazy_operation(self, a, b):
        """Malbolge's crazy operation: crz(a, b)"""
        # Simplified implementation - real Malbolge uses a complex lookup table
        # This is a placeholder for the actual crazy operation
        return (a + b) % 256

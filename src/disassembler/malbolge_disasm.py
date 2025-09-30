class MalbolgeDisassembler:
    """Disassembles Malbolge binary code into human-readable format"""
    
    REVERSE_OPCODES = {
        4: 'jmp',
        5: 'out', 
        23: 'in',
        39: 'rot',
        40: 'mov',
        62: 'add',
        68: 'cra',
        81: 'nop',
        239: 'hlt'
    }
    
    def __init__(self):
        self.memory = []
        self.labels_used = set()
        
    def disassemble_file(self, input_file):
        """Disassemble a Malbolge binary file"""
        with open(input_file, 'rb') as f:
            binary = f.read()
            
        return self.disassemble(binary)
    
    def disassemble(self, binary):
        """Disassemble binary code"""
        self.memory = list(binary)
        disassembly = []
        
        for address, byte in enumerate(self.memory):
            instruction = self.decode_instruction(byte, address)
            disassembly.append(f"{address:04d}: {instruction}")
            
        return '\n'.join(disassembly)
    
    def decode_instruction(self, byte, address):
        """Decode a single instruction"""
        if byte in self.REVERSE_OPCODES:
            return self.REVERSE_OPCODES[byte]
        else:
            return str(byte)

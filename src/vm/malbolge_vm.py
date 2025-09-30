class SimpleMalbolgeVM:
    """A tiny conceptual VM that understands the assembler's simplified encoding.

    Instruction format (simplified): each memory word is a byte. Some instructions
    are followed by an immediate operand in the next memory word.
    """

    def __init__(self):
        self.memory = []
        self.pc = 0
        self.running = False
        self.output = []

    def load(self, data: bytes):
        self.memory = list(data)
        self.pc = 0

    def step(self):
        if self.pc >= len(self.memory):
            self.running = False
            return
        instr = self.memory[self.pc]
        # Simplified mapping - match opcodes from assembler
        if instr == 5:  # out
            # next word is the value to output if present
            val = None
            if self.pc + 1 < len(self.memory):
                val = self.memory[self.pc + 1]
                self.output.append(val)
                self.pc += 2
                return
            else:
                self.running = False
                return
        elif instr == 4:  # jmp
            # operand is next word
            if self.pc + 1 < len(self.memory):
                target = self.memory[self.pc + 1]
                self.pc = target
                return
            else:
                self.running = False
                return
        elif instr == 239:  # hlt
            self.running = False
            return
        else:
            # unknown instruction - treat as data / skip
            self.pc += 1

    def run(self, max_steps=100000):
        self.running = True
        steps = 0
        while self.running and steps < max_steps:
            self.step()
            steps += 1
        return bytes(self.output)

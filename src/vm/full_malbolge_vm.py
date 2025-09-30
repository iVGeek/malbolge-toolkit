from ..assembler.crazy_table import crz

class FullMalbolgeVM:
    """A more featureful conceptual Malbolge VM.

    This VM is still a simplification but introduces:
    - Registers A, C, D
    - Self-modifying memory via the crazy_transform when writing
    - Basic instruction set: out, jmp, mov, add, hlt

    Memory is a list of bytes. Some instructions read a following operand.
    """

    def __init__(self):
        self.memory = []
        self.pc = 0
        self.A = 0
        self.C = 0
        self.D = 0
        self.running = False
        self.output = []

    def load(self, data: bytes):
        self.memory = list(data)
        self.pc = 0

    def read_operand(self):
        if self.pc + 1 < len(self.memory):
            return self.memory[self.pc + 1]
        return 0

    def write_memory(self, addr: int, value: int):
        addr = addr % max(1, len(self.memory))
        # Apply crazy transform with existing memory to mimic self-modification
        old = self.memory[addr]
        new = crz(value, old)
        self.memory[addr] = new

    def step(self):
        if self.pc >= len(self.memory):
            self.running = False
            return
        instr_addr = self.pc
        instr = self.memory[self.pc]
        # decode based on our simplified opcodes
        if instr == 5:  # out
            # output value from A if no operand, else output immediate
            if self.pc + 1 < len(self.memory):
                val = self.memory[self.pc + 1]
                self.output.append(val & 0xFF)
                self.pc += 2
            else:
                self.output.append(self.A & 0xFF)
                self.pc += 1
        elif instr == 4:  # jmp
            if self.pc + 1 < len(self.memory):
                target = self.memory[self.pc + 1]
                self.pc = target
            else:
                self.running = False
        elif instr == 40:  # mov (mov immediate to A for simplicity)
            if self.pc + 1 < len(self.memory):
                val = self.memory[self.pc + 1]
                self.A = val
                self.pc += 2
            else:
                self.running = False
        elif instr == 62:  # add (A = A + immediate)
            if self.pc + 1 < len(self.memory):
                val = self.memory[self.pc + 1]
                self.A = (self.A + val) & 0xFF
                self.pc += 2
            else:
                self.running = False
        elif instr == 239:  # hlt
            self.running = False
        else:
            # treat as data / skip
            self.pc += 1

        # Simple register update rules to simulate Malbolge-like registers
        # C holds previous A, D holds previous C (very simplified)
        self.D = self.C & 0xFF
        self.C = self.A & 0xFF

        # Self-modify the instruction cell that was just executed using crz
        # (value written is the current PC low byte for demonstration)
        try:
            new_val = crz(self.memory[instr_addr], instr_addr & 0xFF)
            self.memory[instr_addr] = new_val
        except Exception:
            # If crz fails for any reason, leave memory unchanged
            pass

    def run(self, max_steps=100000):
        self.running = True
        steps = 0
        while self.running and steps < max_steps:
            self.step()
            steps += 1
        return bytes(self.output)

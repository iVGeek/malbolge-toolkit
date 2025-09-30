class MalbolgeDebugger:
    """A tiny, conceptual step-through debugger for Malbolge programs"""
    
    def __init__(self):
        self.memory = []
        self.pc = 0
        self.running = False
        self.trace = []
        
    def load_program(self, path):
        with open(path, 'rb') as f:
            self.memory = list(f.read())
        self.pc = 0
        print(f"Loaded program: {path} (size={len(self.memory)} bytes)")
        
    def step(self):
        if self.pc >= len(self.memory):
            print("PC out of range")
            self.running = False
            return
        instr = self.memory[self.pc]
        self.trace.append((self.pc, instr))
        print(f"{self.pc:04d}: {instr}")
        self.pc += 1
        
    def run(self):
        self.running = True
        while self.running and self.pc < len(self.memory):
            self.step()
            if len(self.trace) > 1000:
                print("Trace limit reached, stopping")
                break

class TernaryEncoder:
    """Handles conversion to/from Malbolge's ternary representation"""
    
    def __init__(self):
        # Malbolge's trit values
        self.trit_values = [0, 1, 2]
        
    def to_ternary(self, decimal):
        """Convert decimal number to ternary representation"""
        if decimal == 0:
            return [0]
            
        digits = []
        num = decimal
        
        while num > 0:
            digits.append(num % 3)
            num //= 3
            
        return digits[::-1]
    
    def from_ternary(self, ternary_digits):
        """Convert ternary digits to decimal number"""
        result = 0
        for digit in ternary_digits:
            result = result * 3 + digit
        return result
    
    def encode_instruction(self, instruction):
        """Encode instruction in Malbolge's format"""
        # Malbolge uses base-3 representation for instructions
        ternary = self.to_ternary(instruction)
        # Pad to 10 trits (Malbolge's instruction width)
        while len(ternary) < 10:
            ternary.insert(0, 0)
        return ternary

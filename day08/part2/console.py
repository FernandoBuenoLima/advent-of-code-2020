class Instruction:
    def __init__(self, data):
        code, value = data.split()
        self.code = code.strip()
        self.value = int(value.strip())
        self.was_executed = False

class Console:
    def __init__(self, data):
        self.accumulator = 0
        self.pointer = 0
        self.program = list()
        for line in data:
            self.program.append(Instruction(line))
    
    def get_next_instruction(self):
        return self.program[self.pointer]
    
    def execute_next_instruction(self):
        instruction = self.get_next_instruction()
        if instruction.code == 'acc':
            self.accumulator += instruction.value
            self.pointer += 1
        elif instruction.code == 'jmp':
            self.pointer += instruction.value
        elif instruction.code == 'nop':
            self.pointer += 1
        else:
            print("Instruction code not recognized:", instruction.code)
        instruction.was_executed = True
    
    def execute(self):
        while True:
            if self.pointer == len(self.program):
                return self.accumulator
            elif self.get_next_instruction().was_executed:
                return None
            self.execute_next_instruction()
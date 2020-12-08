from console import Console

input = [line.strip() for line in open("input.txt").readlines()]

for i in range(len(input)):
    program = input.copy()
    instruction = program[i]
    code = instruction[:3]
    if code == "nop":
        program[i] = "jmp" + instruction[3:]
    elif code == "jmp":
        program[i] = "nop" + instruction[3:]
    else:
        continue
    console = Console(program)
    answer = console.execute()
    if answer is not None:
        print(answer)
        exit()
    
print("No answer found")
exit()